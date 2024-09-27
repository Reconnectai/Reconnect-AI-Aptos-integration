# Project: Reconnect AI auth service (via Aptos)

## Description

This project is an API for verifying transactions on the Aptos network and generating JWT tokens.
It provides several endpoints for handling transactions and token verification. 
The key features include: 
- JWT token generation based on the verification of signed messages from the Aptos network.
- Transaction status verification on the Aptos blockchain.
- JWT token verification.

## Usage in Reconnect AI

The service is used to generate authorization tokens that 
grant access to the main Reconnect AI API. These tokens are required 
for authenticated requests. Additionally, it is used to validate 
transactions that replenish the internal balance on the API, 
which is measured in a special currency called **Reconnect coin (ReCoin)**. 
This balance can be used to pay for the creation of characters and 
messages within the platform.

### Pricing Policy

The pricing structure for different services on the Reconnect AI platform is as follows:

- Text message: 1 ReCoin
- Audio message: 2 ReCoin
- Video message: 5 ReCoin
- Text-based character: 20 ReCoin
- Audio-based character: 40 ReCoin
- Video-based character: 100 ReCoin

Users can spend their internal ReCoin balance to pay for these services, 
including generating messages or creating characters, depending on the desired format.

### Exchange Rate

The exchange rate for ReCoin is set at 1 ReCoin = 0.01 Aptos. This rate applies when users replenish their internal balance through the platform.