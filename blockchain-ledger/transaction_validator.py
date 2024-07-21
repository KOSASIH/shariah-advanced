from blockchain_api import BlockchainAPI

def validate_transaction(address):
    api = BlockchainAPI()
    compliance = api.get_transaction(address)
    return compliance
