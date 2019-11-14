VERSION=0.2.23
URL=https://github.com/battlesnakeio/engine/releases/download/v$(VERSION)/engine_$(VERSION)_Linux_x86_64.tar.gz

start_engine: release
	cd release; ./engine server

create_game: release
	# Create game and return the game id
	./release/engine create --config snake-config.json | cut -d ':' -f 2 | cut -d '"' -f 2
	
release:
	wget -O release.tar.gz $(URL)
	mkdir release
	tar -C release -xzf release.tar.gz
