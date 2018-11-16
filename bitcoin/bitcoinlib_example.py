import bitcoin.rpc
from bitcoin.core import lx

bitcoin.SelectParams('testnet')

proxy_connection = bitcoin.rpc.Proxy(service_url="http://rpc:rpc1234@projects.koshikraj.com:18332")
# tx_id = lx(input())
# print(proxy_connection.gettransaction(tx_id))

# get current height
cur_block_height = proxy_connection.getblockcount()
print("current blockchain height:", cur_block_height)

# get current height
print("genesis block:", proxy_connection.getblock(proxy_connection.getblockhash(1)))
print("last block:", proxy_connection.getblock(proxy_connection.getblockhash(cur_block_height)))
