#!/bin/bash
export PATH="/home/sol/.local/share/solana/install/releases/v1.18.1-jito"/bin:"$PATH"

BLOCK_ENGINE_URL=https://dallas.testnet.block-engine.jito.wtf
RELAYER_URL=http://dallas.testnet.relayer.jito.wtf:8100
SHRED_RECEIVER_ADDR=147.28.154.132:1002

#	--vote-account /home/sol/vote-account-keypair.json \
exec solana-validator \
	--identity /home/sol/validator-keypair.json \
	--no-voting \
	--known-validator 5D1fNXzvv5NjV1ysLjirC4WY92RNsVH18vjmcszZd8on \
	--known-validator 7XSY3MrYnK8vq693Rju17bbPkCN3Z7KvvfvJx4kdrsSY \
	--known-validator Ft5fbkqNa76vnsjYNwjDZUXoTWpP7VYm3mtsaQckQADN \
	--known-validator 9QxCLckBiJc783jnMvXZubK4wH86Eqqvashtrwvcsgkv \
	--only-known-rpc \
	--log /home/sol/validator-rpc.log \
	--ledger /home/sol/ledger \
	--rpc-port 8899 \
	--dynamic-port-range 8000-8020 \
	--entrypoint entrypoint.testnet.solana.com:8001 \
	--entrypoint entrypoint2.testnet.solana.com:8001 \
	--entrypoint entrypoint3.testnet.solana.com:8001 \
	--wal-recovery-mode skip_any_corrupted_record \
	--limit-ledger-size \
	--tip-payment-program-pubkey DCN82qDxJAQuSqHhv2BJuAgi41SPeKZB5ioBCTMNDrCC \
	--tip-distribution-program-pubkey F2Zu7QZiTYUhPd7u9ukRVwxh7B71oA3NMJcHuCHc29P2 \
	--merkle-root-upload-authority GZctHpWXmsZC1YHACTGGcHhYxjdRqQvTpYkb9LMvxDib \
	--commission-bps 800 \
	--relayer-url ${RELAYER_URL} \
	--block-engine-url ${BLOCK_ENGINE_URL} \
	--shred-receiver-address ${SHRED_RECEIVER_ADDR} \
	--geyser-plugin-config /home/sol/geyser.conf.json \
	--full-rpc-api \
	--enable-rpc-transaction-history \
	--rpc-bind-address 0.0.0.0 \
        --private-rpc \
	--rpc-pubsub-enable-block-subscription 

	# --wait-for-supermajority 254108257 \
	# --expected-bank-hash 4rWEDhTyQVgTw6sPoCthXmUNmjeiwsdKQ5ZNvpEi3uvk \
	# --expected-shred-version 35459

