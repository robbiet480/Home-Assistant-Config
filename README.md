# Home Assistant Configuration

[![Build Status](https://travis-ci.org/robbiet480/Home-Assistant-Config.svg?branch=master)](https://travis-ci.org/robbiet480/Home-Assistant-Config)

## Hardware
Yes, I name my servers after rappers...

### "biggie"

`biggie` runs VMWare ESXi 5 and the following two virtual machines:
  - [pfSense 2.3][pfsense]
  - [FreeNAS 9][freenas]

It's primary function is as a router and as a NAS, mostly storing media (TV, movies, music) as well as a backup target for computers.

#### Specs

- [SuperMicro X10SL7-F][supermicro-x10sl7-f]
  - [Intel(R) Xeon(R) CPU E3-1220 v3 @ 3.10GHz][intel-e3-1220-v3]
  - 32GB RAM
  - ESXi runs off a USB key directly connected to the motherboard
  - 2x 120GB SSDs as boot drives for the virtual machines
  - 8 [4TB Seagate NAS hard drives][seagate-hdd]


### "bigsean"

`bigsean` runs Ubuntu 16.04 LTS and is the primary home automation system.

#### Specs

- [SuperMicro A1SRi-2758F-O][supermicro-a1sri-2758f]
  - Integrated Intel Atom C2750 "Avoton" Octa-Core
  - 32GB RAM
  - 2x256GB SSD
  - 4x gigabit ethernet
  - [Aeotec ZW090 Z-Wave Stick][aeotec-zstick]
  - [Tripp Lite 1500VA UPS Back Up, AVR, LCD Display, 10 Outlets, 120V 900W, Tel & Coax Protection, USB (SMART1500LCDT)][tripp-lite-ups]

### Misc
- Wireless is provided by a [Ubiquiti Networks Unifi 802.11ac Dual-Radio PRO Access Point][uap-ac-pro-us]
- Ethernet is all connected via a [TP-Link 48-Port Gigabit Ethernet Rackmount Switch][tplink-switch]

## Software
- [Home Assistant](https://home-assistant.io/), always running the dev branch, it gets updated a couple times a week.
- [Homebridge][homebridge]
- [homebridge-homeassistant][homebridge-homeassistant]
- [Network UPS Tools (NUT)][nut]
- [Plex Media Server][plex]
- [InfluxDB][influxdb] for data collection
- [Grafana][grafana] for graphing
- [Mosquitto][mosquitto] for MQTT

## People
- [Robbie][robbie-twitter]
  - MacBook Pro
  - iPhone 7 Plus
- [Brandon][brandon-twitter]
  - MacBook Pro
  - iPhone 7

## Devices
Devices are broken down by room

### Entrance Hallway
- [EcoLink Door/Window Sensor (DWZWAVE2-ECO)][ecolink-door-sensor]
- [Linear/GoControl/2gig WS15Z-1 Z-Wave Switch][linear-ws15z-1] - next to front door
- [Linear/GoControl/2gig WT00Z-1 Z-Wave 3-Way Accessory Switch][linear-wt00z-1] - at far end of hallway

### Kitchen
- 3 [Linear GoControl WS15Z-1 Z-Wave Switch][linear-ws15z-1]
  - Overhead Lights
  - Counter Lights
  - Under Cabinet Lights

### Living Room
- [HomeSeer HS-WD100+ Z-Wave Plus Scene-Capable Wall Dimmer][hs-wd100+] - controls lights over dining table
- [Aeotec ZW100 Multisensor][multisensor] - mounted high up in corner of room
- [Philips Hue Lightstrip (1st Generation)][hue-lightstrip] - under counter
- [Amazon Echo][amazon-echo]
- 2 [Philips Hue White and Color Ambiance Light Bulb, A19][hue-bulb] - in lights on either side of the couch
- [Sony XBR65X850D 65-Inch 4K Ultra HD Smart TV (2016 model)][sony-xbr65x850d-tv]
  - Android TV
  - [Notifications for Android TV][nfatv] installed
- [Onkyo TX-NR616 7.2- Channel Network A/V Receiver][onkyo-tx-nr616]
  - 2 [Klipsch RF-42 II Floorstanding Speaker][klipsch-rf42]
  - 2 [Klipsch RB-41 II Bookshelf Speaker][klipsch-rb41]
  - [Klipsch Sub-12 12-inch 300W Subwoofer][klipsch-sub-12]
  - [Klipsch RC-42 II Center Channel][klipsch-rc42]
- [Sonos CONNECT][sonos-connect]
- [Apple TV, 4th Generation, 32GB][apple-tv]
- [Chromecast (2nd Generation)][chromecast]
- [iTach IP2IR (unused)][itach-ip2ir]
- [PlayStation TV][pstv]

### Guest Bathroom
- [Amazon Echo Dot][amazon-echo-dot]
- [UE Roll (1st Generation)][ue-roll] - paired with Echo Dot via Bluetooth
- [Withings Body Cardio - Heart Health and Body Composition Wi-Fi Scale, Black][withings-scale]

### Interior Hallway
- [Philips Hue Bloom][hue-bloom]
- [Linear/GoControl/2gig WS15Z-1 Z-Wave Switch][linear-ws15z-1] - next to Living Room Dimmer
- [Linear/GoControl/2gig WT00Z-1 Z-Wave 3-Way Accessory Switch][linear-wt00z-1] - at far end of hallway
- [Enerwave ZWN-BPC Z-Wave Motion Sensor][enerwave-zwn-bpc]
- All hardware listed at the top of this README is on a desk in the interior hallway

### Robbie's Room
- [EcoLink Door/Window Sensor (DWZWAVE2-ECO)][ecolink-door-sensor]
- [Aeotec ZW100 Multisensor][multisensor] - mounted high up in corner of room above desk
- 3 [Philips Hue White and Color Ambiance Light Bulb, A19][hue-bulb]
  - Floorstanding lamp next to desk
  - Left and right sides of bed, mounted at head level in an IKEA MINUT wall lamp
- [Philips Hue Lightstrip (1st Generation)][hue-lightstrip] - under desk
- [RGB LED Strip with Wifi Controller][rgb-led-strip] - On ledge under window to right of bed
- [Amazon Echo][amazon-echo]
- [Sonos PLAY:3][sonos-play3]
- [ZEEQ Smart Pillow][zeeq-pillow]
- [Toshiba 55WX800U 55-Inch 1080p 240 Hz Cinema Series 3D LED TV, Black (2010 Model)][toshiba-55wx800u]
- [Apple TV, 4th Generation, 32GB][apple-tv]
- [Roku 3 Streaming Media Player][roku-3]
- [Sony PlayStation 4 500GB Console][playstation-4]
- [Raspberry Pi 3 Model B][raspi] - used to control devices via CEC
- 2 [VSTARCAM 720p cameras][vstarcam] - pointed out the windows for a view of [Lake Merritt][lake-merritt] and [construction happening in the surrounding few blocks][bvdsp]

## Automations
- End of day sunset notification
- Front door is open
- Notify if motion detected in Living Room or Hallway when no one is home
- Notify if Robbie's door is opened when he isn't home
- Notify if there is motion in Robbie's Room when he isn't home
- Robbie arrived home
- Robbie left home
- Send a notification 1 hour before sunset
- Send notifications for guests/misc calls from front desk
- Send notifications for package delivery
- Someone arrived home
- Someone left home
- Turn off all devices when everyone leaves home
- Turn off living room lights when Apple TV is playing
- Turn off Robbie's Room lights when Apple TV, Chromecast or Roku is playing
- Turn on entrance hallway overhead when the door opens
- Turn on hallway lights when there is movement at night
- Turn on living room lights when Apple TV is paused
- Turn on Robbie's Room lights when Apple TV, Chromecast or Roku is paused

## TODOs
See [issues](https://github.com/robbiet480/Home-Assistant-Config/issues).

[homebridge]: https://github.com/nfarina/homebridge
[homebridge-homeassistant]: https://github.com/home-assistant/homebridge-homeassistant
[nut]: http://networkupstools.org/
[plex]: https://www.plex.tv/
[influxdb]: https://www.influxdata.com/
[robbie-twitter]: https://twitter.com/robbie
[brandon-twitter]: https://twitter.com/bitsofbrandon
[linear-ws15z-1]: http://amzn.to/2l1ZwMu
[ecolink-door-sensor]: http://amzn.to/2kfzKVq
[linear-wt00z-1]: http://amzn.to/2l6qX7B
[hs-wd100+]: http://amzn.to/2kUUSgL
[multisensor]: http://amzn.to/2kiWcrJ
[hue-lightstrip]: http://amzn.to/2kV11JM
[amazon-echo]: http://amzn.to/2kFpGUm
[hue-bulb]: http://amzn.to/2kVba9w
[sony-xbr65x850d-tv]: http://amzn.to/2kV4WpU
[nfatv]: https://play.google.com/store/apps/details?id=de.cyberdream.androidtv.notifications.google&hl=en
[onkyo-tx-nr616]: https://www.amazon.com/Onkyo-TX-NR616-Receiver-Discontinued-Manufacturer/dp/B0077V88W2/
[klipsch-rf42]: http://www.klipsch.com/products/rf-42-ii-floorstanding-speaker
[klipsch-rb41]: http://www.klipsch.com/products/rb-41-ii-bookshelf-speakers-pair
[klipsch-sub-12]: http://amzn.to/2kFH77b
[klipsch-rc42]: http://amzn.to/2kFxbuk
[sonos-connect]: http://amzn.to/2kV3xzB
[apple-tv]: http://www.apple.com/shop/buy-tv/apple-tv/apple-tv-32gb
[chromecast]: https://www.google.com/chromecast/tv/chromecast/
[itach-ip2ir]: http://amzn.to/2kFxvcw
[pstv]: http://amzn.to/2kV40lm
[amazon-echo-dot]: http://amzn.to/2kfGti9
[ue-roll]: http://amzn.to/2kiRf2k
[withings-scale]: http://amzn.to/2kiVJG1
[hue-bloom]: http://amzn.to/2ky5TDD
[enerwave-zwn-bpc]: http://amzn.to/2kFI3sd
[rgb-led-strip]: http://amzn.to/2kFQYKb
[sonos-play3]: http://amzn.to/2l6ldKM
[toshiba-55wx800u]: https://www.amazon.com/Toshiba-55WX800U-55-Inch-1080p-Cinema/dp/B00447GA2W/
[zeeq-pillow]: https://www.kickstarter.com/projects/2121327950/zeeq-smart-pillow-stream-music-stop-snoring-sleep
[roku-3]: http://amzn.to/2l6im4I
[playstation-4]: https://www.amazon.com/Sony-PlayStation-4-500GB-Console/dp/B00BGA9WK2/
[raspi]: http://amzn.to/2kFCrhz
[vstarcam]: http://amzn.to/2kfzs0U
[lake-merritt]: https://en.wikipedia.org/wiki/Lake_Merritt
[bvdsp]: http://www.oaklandnet.com/bvdsp/
[supermicro-a1sri-2758f]: http://amzn.to/2l6vc2S
[aeotec-zstick]: http://amzn.to/2kV8loA
[tripp-lite-ups]: http://amzn.to/2kFEjqI
[uap-ac-pro-us]: http://amzn.to/2kj3IDf
[tplink-switch]: http://amzn.to/2kFAuBC
[supermicro-x10sl7-f]: http://amzn.to/2kfGaUt
[intel-e3-1220-v3]: http://amzn.to/2kFBk1y
[seagate-hdd]: http://amzn.to/2kiUJlq
[pfsense]: https://www.pfsense.org
[freenas]: http://www.freenas.org/
[grafana]: https://grafana.net/
[mosquitto]: https://mosquitto.org/
