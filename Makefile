VERSION=0.2.23
URL=https://github.com/battlesnakeio/engine/releases/download/v$(VERSION)/engine_$(VERSION)_Linux_x86_64.tar.gz

release:
	wget -O release.tar.gz $(URL)
	mkdir release
	tar -C release -xzf release.tar.gz
