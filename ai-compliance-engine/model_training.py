from shariah_compliance_model import ShariahComplianceModel
from data_preprocessing import preprocess_data

def train_model(data):
    model = ShariahComplianceModel()
    data = preprocess_data(data)
    model.train(data)
    return model
