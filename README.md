# zksync_api
How to get transactions data on the ZKsync mainnet for Open Data Community Hackathon

The Open Data Community participants that are mostly come from Data Science background, so it is very possible that they do not know how to get data from blockchains like ethereum, zksync etc. and it will be time consuming work to understand it. So I decided to prepare an end to end guide with source code to explain how to get data from ZKsync blockchain that even maybe be a little harder to work with it, and by this tutorial make this procedure easier for them.

Methodology : 
There are multiple ways to get data of transactions from ZKsync but the best simple one and fast one is using ZKsync official APIs that we are going to use in this tutorial.
Link : https://api.zksync.io/api/v0.2/ - mainnet api v0.2
And also we will use python language beacuse most of the Data Scientists and particapents of hackathon use python as the main tool for development.



Source Code and Implementation: 
We will use api v0.2 of zksync for getting transactions data which is a rest API and you can find docs here : https://docs.zksync.io/apiv02-docs/
There are a lot of endpoints for different purposes but for this tutorial our focus will be on getting transactions data of one specific account in blockchain, which is very important for hackathon participants to use this for sybil detection algorithms etc.

before starting to explain the source code we need to install requests package, that we will be using to working with APIs with this commend : pip install requests 

Now lets dive into the code: 
