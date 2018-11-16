# Bitcoin Core basics

## Quick start

### Install from source

Clone the Bitcoin Core source code from https://github.com/bitcoin/bitcoin.git. 

1. Execute the shell script : 

    `./autogen.sh` 

2. Run the configuration script: 

    `./configure` 

3. Compile the source code and run the executable: 

    ```
    make 

    make install 
    ```
    
4. Run the Bitcoin daemon: 

    `bitcoind -daemon`

### Install using PPA (Ubuntu distro)

    sudo add-apt-repository ppa:bitcoin/bitcoin
    sudo apt-get update
    sudo apt-get install bitcoind

### Other platforms
[https://bitcoin.org/en/full-node](https://bitcoin.org/en/full-node)

### Interact with Bitcoin node

Get blockchain info command run on a public node
```
bitcoin-cli -rpcconnect=projects.koshikraj.com -rpcport=18332 -rpcuser=rpc -rpcpassword=rpc1234 getblockchaininfo
```