# PerimeterX-Reverse

*Background Information*

This repo is gonna be my progress as I continue to attempt to reverse engineer PerimeterX's challenge untill I can produce a fully unflagged bypass/solver that's completley automated using only request no browser.
I plan to scrape Device WEBGL Fingerprints and make my own Motion Data if needed.

*How can I try to avoid getting prompted with this PerimeterX captcha?*

- **Use High Quality IP Addresses** | low fraud score, residential IP (best)
- **Use Undetected Drivers** | If you're using something such as selenium, puppeteer or even playwright it's very important you use an "undetected" plugin that actually works to try and avoid getting prompted (99% of the time it is very easy for these antibot services to tell you're using a webdriver like selenium, puppeteer, playwright, phantom and etc even when using an "undetected" version, personally i would advise staying away from these when trying to bypass captchas.)
- **Unflagged TLS** | It is important to insure that your request is not being flagged due to its TLS Fingerprint. One way you can try to avoid this is to use a library that allows you to modify your TLS properties such as TLS_CLIENT which allows you to spoof some of your properties such as extension order, supported cipher suites and some basic window properties. Please note this will not always be enough to not get prompted with antibot challenges.
- **Unflagged WEBGL/Device Fingerprints** | If the antibot service you're trying to get around is any good it will check something called a device hash/fingerprint that was computed from data collected from properties it was able to gather from you visiting the site. Suprisingly, the computed fingerprint is usually very unique (only 1 in around 200,000 devices produce the same hash) this makes it easy to tell the antibot services if your request is coming from a client with the same browser properties (CPU, GPU, CanvasFP, Screen Resolution, Screen Dimensions, User-Agent, Browser Extensions, Timezone just to name a few) as you can see you can't spoof these types of things with only a request library which is where things get more complex and why it may be required to reverse engineer the antibot's encryption methods and fingerprint methods so you're able to spoof these properties.  


# How it works # 

**PerimeterX Challenge Example** (shown on ssense.com)

![image](https://github.com/Pr0t0ns/PerimeterX-Reverse/assets/105520163/34c8ebf9-b4af-47bf-8a00-1d16d43cf474)

**PX Cookie Gets set by PerimeterX Script**

![image](https://github.com/Pr0t0ns/PerimeterX-Reverse/assets/105520163/8e0f6988-3dd9-4110-a2a7-b08ee35b7776)

**Script that sets the Cookie gets loaded within HTML <script> tag**

![image](https://github.com/Pr0t0ns/PerimeterX-Reverse/assets/105520163/9905f2bb-29c5-44d7-abdb-6c2a73376783)

As you can see it shows the *PxAPPID* which is essentially the sites site_key

**Request to fetch the challenge script**

![image](https://github.com/Pr0t0ns/PerimeterX-Reverse/assets/105520163/f8de9077-5205-4c1f-b06c-10cdc202519d)

**Source Code of PerimeterX's loaded challenge**

![image](https://github.com/Pr0t0ns/PerimeterX-Reverse/assets/105520163/cde4099b-bfda-4041-9438-ac53c98b46d2)

The source code is over 9,000 lines long but this is because it's obfuscated and it has a lot of polyfill functions. 
one thing you should note is that the source code has VM protection along with obfuscation, meaning that every time you refresh the page the function and variable names will change. PerimeterX along with many other antibot services use this to make it as difficult as possible for people to reverse engineer.

# What we need to do #

**Solve Request**

![image](https://github.com/Pr0t0ns/PerimeterX-Reverse/assets/105520163/6012978b-9d52-498b-8520-bf7594525b20)

This request essentially whitelist the set *_pxhd* cookie so that it is valid. So basically this is the captcha token. all we have to do is reverse the payload values so we can automate this.

**Payload Value**

![image](https://github.com/Pr0t0ns/PerimeterX-Reverse/assets/105520163/360a05ce-f3b0-4018-80cc-27f5d7dbe97b)

These are the payload values

* `payload` Encrypted & Encoded value I will need to reverse engineer (We can tell that base64 was used at some point because we can see an "=" which usually comes from padding)
* `AppID` this is basically the site key mentioned earlier (each site has a unique one of these)
* `tag` this is the version tag (each site also has a unique version)
* `uuid` randomly generated UUID this is usually just used as a request indentifier
* `ft` A unique 3 digit number (each site has it's unique ft number)
* `seq`*0* always.
* `en` *NTA* always.
* `pc` Generated Value I will need to reverse
* `sid` **TO BE DETERMINED**
* `vid` **TO BE DETERMINED**
* `pxhd` This is the *_pxhd* cookie value which is basically the captcha token
* `cts` **TO BE DETERMINED**
* `rsc` This is the Request Count
