
comandos = {'ben': 'Devuelve este mensaje de ayuda',
            'blue': 'Devuelve el valor del dolar blue hasta la fecha',
            'usdt': 'Devuelve el valor del USDT en distintos exchanges',
            'oficial': 'Devuelve el valor del dolar oficial hasta la fecha',
            'tarjeta': 'Devuelve el valor del dolar tarjeta hasta la fecha',
            'card': 'Convierte un valor dado a pesos tomando el dolar tarjeta. Ej: `?card 100`',
            'usdars': 'Convierte un valor dado a pesos tomando el dolar blue. Ej: `?usdars 100`',
            'tax': 'Convierte un valor en pesos sin impuestos a uno con los impuestos incluidos. Ej: `?tax 2500`',
            'bio': 'Te cuenta un poco de la biografia de Franklin. `?bio eng` para ingles, no hace falta pasar nada mas para castellano',
            'price': 'Devuelve el valor de una cryto que pases. Tenes que pasarme el simbolo y en que queres que te de el precio. Ej: `?price btc busd`, el segundo argumento es opcional, por defecto lo muestro en USDT(`?price eth`)',
            'meme': 'Devuelve un meme random'
            
            }



# Continuara, tiene que haber una mejor forma de hacer esto pero me dio paja en ese momento xd
img_coins = {   'BINANCE_LOGO': 'https://public.bnbstatic.com/image/cms/blog/20200707/631c823b-886e-4e46-b12f-29e5fdc0882e.png',
                '1INCH':        'https://research.binance.com/static/images/projects/1inch/logo.png',
                'AAVE':         'https://research.binance.com/static/images/projects/aave-protocol/logo2.png',
                'ACM':          'https://research.binance.com/static/images/projects/ac-milan-fan-token/logo.png',
                'ADA':          'https://research.binance.com/static/images/projects/cardano/logo.png',
                'ALGO':         'https://research.binance.com/static/images/projects/algorand/algorand%20logo.png',
                'ALICE':        'https://research.binance.com/static/images/projects/my-neighbor-alice/logo.png',
                'ANKR':         'https://research.binance.com/static/images/projects/ankr-network/logo.jpg',
                'APPC':         'https://research.binance.com/static/images/projects/appcoins/logo.png',
                'AR':           'https://research.binance.com/static/images/projects/arweave/logo.png',
                'ARK':          'https://research.binance.com/static/images/projects/ark/logo.png',
                'ARN':          'https://research.binance.com/static/images/projects/aeron/logo2.png',
                'ARPA':         'https://research.binance.com/static/images/projects/arpa/logo.png',
                'ASR':          'https://research.binance.com/static/images/projects/asr-fan-token/logo.png',
                'ATA':          'https://research.binance.com/static/images/projects/automata-network/logo.png',
                'ATM':          'https://research.binance.com/static/images/projects/atm-fan-token/logo.png',
                'ATOM':         'https://research.binance.com/static/images/projects/cosmos-network/cosmoslogo.png',
                'AUTO':         'https://research.binance.com/static/images/projects/auto/logo.png',

                'BADGER':       'https://research.binance.com/static/images/projects/badger-dao/logo.png',
                'BAKE':         'https://research.binance.com/static/images/projects/bakerytoken/logo.png',
                'BAR':          'https://research.binance.com/static/images/projects/fc-barcelona-fan-token/logo.png',
                'BAT':          'https://research.binance.com/en/projects/basic-attention-token',
                'BCH':          'https://research.binance.com/static/images/projects/bitcoin-cash/logo.png',
                'BCD':          'https://research.binance.com/static/images/projects/bitcoin-diamond/logo.png',
                'BGBP':         'https://research.binance.com/static/images/projects/binance-gbp/logo.png',
                'BIDR':         'https://research.binance.com/static/images/projects/binance-idr/logo.png',
                'BKRW':         'https://research.binance.com/static/images/projects/binance-krw/logo.png',
                'BNB':          'https://research.binance.com/static/images/projects/bnb/logo.png',
                'BTC':          'https://research.binance.com/static/images/projects/bitcoin/logo.png',
                'BTG':          'https://research.binance.com/static/images/projects/bitcoin-gold/logo.png',
                'BTT':          'https://research.binance.com/static/images/projects/bittorrent/logo.png',
                'BURGER':       'http://research.binance.com/static/images/projects/burger-swap/logo.png',
                'BUSD':         'https://research.binance.com/static/images/projects/binance-usd/logo2.png',

                'CITY':         'https://research.binance.com/static/images/projects/manchester-city-fan-token/logo.png',

                'DAI':          'https://research.binance.com/static/images/projects/dai/logo.png',
                'DASH':         'https://research.binance.com/static/images/projects/dash/logo.png',
                'DATA':         'https://research.binance.com/static/images/projects/streamr-network/logo.png',
                'DENT':         'https://research.binance.com/static/images/projects/dent/logo.png',
                'DGB':          'https://research.binance.com/static/images/projects/digibyte/digibyte-logo.png',
                'DOCK':         'https://research.binance.com/static/images/projects/dock/logo.png',
                'DODO':         'https://research.binance.com/static/images/projects/dodo/logo.png',
                'DOGE':         'https://research.binance.com/static/images/projects/dogecoin/logo.png',
                'DOT':          'https://research.binance.com/static/images/projects/polkadot/logo.png',
                'DREP':         'https://research.binance.com/static/images/projects/drep/logo.png',

                'CAKE':         'https://research.binance.com/static/images/projects/pancakeswap/logo.png',
                'CHZ':          'https://research.binance.com/static/images/projects/chiliz/logo.png',
                'CKB':          'https://research.binance.com/static/images/projects/nervos-network/logo.png',
                
                'ENJ':          'https://research.binance.com/static/images/projects/enjin-coin/logo.png',
                'ETC':          'https://research.binance.com/static/images/projects/ethereum-classic/logo.png',
                'ETH':          'https://research.binance.com/static/images/projects/ethereum/icon.png',

                'FIRO':         'https://research.binance.com/static/images/projects/firo/logo.png',
                'FUEL':         'https://research.binance.com/static/images/projects/etherparty/logo.png',
                'FUN':          'https://research.binance.com/static/images/projects/funfair/logo.png',

                'GNT':          'https://research.binance.com/static/images/projects/golem/logo.png',
                'GTC':          'https://research.binance.com/static/images/projects/gitcoin/logo.png',
                'GTO':          'https://research.binance.com/static/images/projects/gifto/logo.png',

                'HOT':          'https://research.binance.com/static/images/projects/holochain/logo.png',
                
                'ICP':          'https://research.binance.com/static/images/projects/dfinity/logo.png',
                'IOTA':         'https://research.binance.com/static/images/projects/iota/logo.png',

                'JUV':          'https://research.binance.com/static/images/projects/juventus-fan-token/logo.png',

                'LINK':         'https://research.binance.com/static/images/projects/chainlink/logo2.png',
                'LTC':          'https://research.binance.com/static/images/projects/litecoin/logo.png',
                'LUN':          'https://research.binance.com/static/images/projects/lunyr/logo.png',
                'LUNA':         'https://research.binance.com/static/images/projects/terra/logo.png',

                'MANA':         'https://research.binance.com/static/images/projects/decentraland/logo.png',
                'MASK':         'https://research.binance.com/static/images/projects/mask-network/logo.png',
                'MATIC':        'https://research.binance.com/static/images/projects/matic-network/logo.png',

                'NANO':         'https://research.binance.com/static/images/projects/nano/nano-logo.png',
                'NU':           'https://research.binance.com/static/images/projects/nucypher/logo.png',

                'ORN':          'https://research.binance.com/static/images/projects/orion-protocol/logo.png',

                'POLY':         'https://research.binance.com/static/images/projects/polymath/logo.png',
                'PSG':          'https://research.binance.com/static/images/projects/paris-saint-germain-fan-token/logo.png',

                'RVN':          'https://research.binance.com/static/images/projects/ravencoin/logo.png',
                'ROSE':         'https://research.binance.com/static/images/projects/oasis-network/logo1.png',
                
                'SHIB':         'https://research.binance.com/static/images/projects/shiba-inu/logo.png',
                'SKY':          'https://research.binance.com/static/images/projects/skycoin/logo.png',
                'SLP':          'https://research.binance.com/static/images/projects/small-love-potion/logo.png',
                'SOL':          'https://research.binance.com/static/images/projects/solana/logo2.png',
                'SPARTA':       'https://research.binance.com/static/images/projects/spartan-protocol/logo.png',
                'SUSD':         'https://research.binance.com/static/images/projects/susd/logo.png',
                'SUSHI':        'https://research.binance.com/static/images/projects/sushi/logo.png', 

                'TFUEL':        'https://research.binance.com/static/images/projects/theta-fuel/logo.png',
                'THETA':        'https://research.binance.com/static/images/projects/theta-network/thetalogo.jpg',
                'TKO':          'https://research.binance.com/static/images/projects/tokocrypto/logo.png',
                'TLM':          'https://research.binance.com/static/images/projects/alien-worlds/logo.png',
                'TRX':          'https://research.binance.com/static/images/projects/tron/tronlogo.png',
                'TUSD':         'https://research.binance.com/static/images/projects/trueusd/logo.png',
                

                'UNI':          'https://research.binance.com/static/images/projects/uniswap/logo.png',
                'USDC':         'https://research.binance.com/static/images/projects/usd-coin/logo.png',
                'USDS':         'https://research.binance.com/static/images/projects/stable-usd/logo.png',
                'USDT':         'https://research.binance.com/static/images/projects/usd-tether/logo.png',

                'VET':          'https://research.binance.com/static/images/projects/vechain/logo.png',

                'WIN':          'https://research.binance.com/static/images/projects/wink/logo2.png',

                'XLM':          'https://research.binance.com/static/images/projects/stellar-lumens/logo.png',
                'XMR':          'https://research.binance.com/static/images/projects/monero/logo.png',
                'XRP':          'https://research.binance.com/static/images/projects/xrp/logo.png',

                'ZEC':          'https://research.binance.com/static/images/projects/zcash/logo.png',
                  
            }

projects = {    'PROJECTS':     'https://research.binance.com/en/projects',
                'ADA':          'https://research.binance.com/en/projects/cardano',
                'BCH':          'https://research.binance.com/en/projects/bitcoin-cash',
                'BNB':          'https://research.binance.com/en/projects/bnb',
                'BTC':          'https://research.binance.com/en/projects/bitcoin',
                'DOGE':         'https://research.binance.com/en/projects/dogecoin',
                'ETC':          'https://research.binance.com/en/projects/ethereum-classic',
                'ETH':          'https://research.binance.com/en/projects/ethereum',
                'GTC':          'https://research.binance.com/en/projects/gitcoin',
                'ICP':          'https://research.binance.com/en/projects/dfinity',
                'LTC':          'https://research.binance.com/en/projects/litecoin',
                'SHIB':         'https://research.binance.com/en/projects/shiba-inu',
                'XMR':          'https://research.binance.com/en/projects/monero',
                'XRP':          'https://research.binance.com/en/projects/xrp',


            }
