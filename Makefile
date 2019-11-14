VERSION=0.2.23
PLATFORM=Linux
#PLATFORM=Darwin
URL=https://github.com/battlesnakeio/engine/releases/download/v$(VERSION)/engine_$(VERSION)_$(PLATFORM)_x86_64.tar.gz

start_engine: release
	cd release; ./engine server

create_game: release
	# Create game and return the game id
	./release/engine create --config snake-config.json | cut -d ':' -f 2 | cut -d '"' -f 2
	
release: release.tar.gz
	mkdir release
	tar -C release -xzf release.tar.gz

release.tar.gz:
	wget -O release.tar.gz $(URL)
