from web3 import Web3

class BlockchainAPI:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'))

    def add_transaction(self, address, compliance):
        contract = self.w3.eth.contract(address='0x...YOUR_CONTRACT_ADDRESS...', abi=[...])
        tx_hash = contract.functions.addTransaction(address, compliance).transact()
        return tx_hash

    def get_transaction(self, address):
        contract = self.w3.eth.contract(address='0x...YOUR_CONTRACT_ADDRESS...', abi=[...])
        compliance = contract.functions.getTransaction(address).call()
        return compliance
