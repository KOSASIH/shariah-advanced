from fabric_sdk_py import FabricSDK

class HyperledgerFabric:
    def __init__(self):
        self.sdk = FabricSDK()

    def create_channel(self, channel_name):
        self.sdk.create_channel(channel_name)

    def join_channel(self, channel_name, peer_name):
        self.sdk.join_channel(channel_name, peer_name)

    def install_chaincode(self, channel_name, chaincode_name, chaincode_version):
        self.sdk.install_chaincode(channel_name, chaincode_name, chaincode_version)

    def instantiate_chaincode(self, channel_name, chaincode_name, chaincode_version):
        self.sdk.instantiate_chaincode(channel_name, chaincode_name, chaincode_version)

    def invoke_chaincode(self, channel_name, chaincode_name, function_name, args):
        self.sdk.invoke_chaincode(channel_name, chaincode_name, function_name, args)

    def query_chaincode(self, channel_name, chaincode_name, function_name, args):
        self.sdk.query_chaincode(channel_name, chaincode_name, function_name, args)
