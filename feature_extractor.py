import torch
import torch.nn.functional as F
from torchvision import models, transforms
from transformers import AutoModel, AutoTokenizer
from PIL import Image
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class FeatureExtractor:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.image_transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        self.resnet = models.resnet50(pretrained=True)
        self.resnet = torch.nn.Sequential(*(list(self.resnet.children())[:-1])).to(self.device).eval()
        self.tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
        self.text_model = AutoModel.from_pretrained('bert-base-uncased').to(self.device).eval()

    def image_to_vector(self, image_path):
        image = Image.open(image_path)
        image_tensor = self.image_transform(image).unsqueeze(0).to(self.device)
        with torch.no_grad():
            features = self.resnet(image_tensor)
        features = F.normalize(features, p=2, dim=1)
        return features.cpu().numpy().flatten()

    def text_to_vector(self, text):
        inputs = self.tokenizer(text, return_tensors='pt').to(self.device)
        with torch.no_grad():
            outputs = self.text_model(**inputs)
        features = torch.mean(outputs.last_hidden_state, dim=1)
        features = F.normalize(features, p=2, dim=1)
        return features.cpu().numpy().flatten()
