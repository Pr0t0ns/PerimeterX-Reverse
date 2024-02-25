# PerimiterX-Reverse

*Background Information*

This repo is gonna be my progress as I continue to attempt to reverse engineer PerimiterX's challenge untill I can produce a fully unflagged bypass/solver that's completley automated using only request no browser.
I plan to scrape Device WEBGL Fingerprints and make my own Motion Data if needed.

*How can I try to avoid getting prompted with this PerimiterX captcha?*

- **Use High Quality IP Addresses** | low fraud score, residential IP (best)
- **Use Undetected Drivers** | If you're using something such as selenium, puppeteer or even playwright it's very important you use an "undetected" plugin that actually works to try and avoid getting prompted (99% of the time it is very easy for these antibot services to tell you're using a webdriver like selenium, puppeteer, playwright, phantom and etc even when using an "undetected" version, personally i would advise staying away from these when trying to bypass captchas.)
- **Unflagged TLS** | It is important to insure that your request is not being flagged due to its TLS Fingerprint. One way you can try to avoid this is to use a library that allows you to modify your TLS properties such as TLS_CLIENT which allows you to spoof some of your properties such as extension order, supported cipher suites and some basic window properties. Please note this will not always be enough to not get prompted with antibot challenges.
- **Unflagged WEBGL/Device Fingerprints** | If the antibot service you're trying to get around is any good it will check something called a device hash/fingerprint that was computed from data collected from properties it was able to gather from you visiting the site. Suprisingly, the computed fingerprint is usually very unique (only 1 in around 200,000 devices produce the same hash) this makes it easy to tell the antibot services if your request is coming from a client with the same browser properties (CPU, GPU, CanvasFP, Screen Resolution, Screen Dimensions, User-Agent, Browser Extensions, Timezone just to name a few) as you can see you can't spoof these types of things with only a request library which is where things get more complex and why it may be required to reverse engineer the antibot's encryption methods and fingerprint methods so you're able to spoof these properties.  



**PerimiterX Challenge Example** (shown on zillow.com)

![image](https://github.com/Pr0t0ns/PerimiterX-Reverse/assets/105520163/57068aca-2523-415b-b194-6c5febcb34cb)
