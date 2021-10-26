# made by @Yisus7u7

CC ?= clang++
PREFIX ?= /data/data/com.termux/files/usr
HOME ?= /data/data/com.termux/files/home
LIB = ./src/tmsd.cpp


all: compile


compile:
	@echo "Compiling target tmsd.cpp"
	$(CC) -Wall $(LIB) -o lib-termux-mate-settings-daemon.so
	@echo "Linking target lib-termux-mate-settings-daemon.so"
	@echo "Done. Run make install for install"
	
	
install: compile
	mkdir -p $(PREFIX)/lib
	mkdir -p $(PREFIX)/bin
	mkdir -p $(PREFIX)/share/tmsd
	mkdir -p $(HOME)/.config/autostart
	cp ./lib-termux-mate-settings-daemon.so $(PREFIX)/lib/lib-termux-mate-settings-daemon.so
	chmod +x ./tmsd
	chmod +x ./tmsd-gui
	cp ./tmsd $(PREFIX)/bin/tmsd
	cp ./tmsd-gui $(PREFIX)/bin/tmsd-gui
	cp ./*.py $(PREFIX)/share/tmsd/
	cp ./*.png $(PREFIX)/share/tmsd/
	cp -rf ./theme $(PREFIX)/share/tmsd
	cp ./org.tmsd.github.desktop $(PREFIX)/share/applications/org.tmsd.github.desktop
	cp ./org.termux-mate-settings-daemon.desktop $(HOME)/.config/autostart/org.termux-mate-settings-daemon.desktop
	
uninstall:
	rm -rf $(PREFIX)/lib/lib-termux-mate-settings-daemon.so
	rm -rf $(PREFIX)/bin/tmsd
	rm -rf $(PREFIX)/bin/tmsd-gui
	rm -rf $(PREFIX)/share/tmsd
	rm -rf $(PREFIX)/share/applications/org.tmsd.github.desktop
	rm -rf $(HOME)/.config/autostart/org.termux-mate-settings-daemon.desktop
	
clean:
	rm -rf ./*.so

.PHONY: all compile install uninstall clean
