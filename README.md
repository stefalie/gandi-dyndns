# gandi-dyndns

A minimalist approach to pointing an A record on Gandi's LiveDNS to your router's IP address.

You need to assign your Gandi API key to `api_key`.

You might want to run this as cron job.
Edit crontab:

```
sudo crontab -e
```

Then, for example, add something like this to run the update script at reboot and every 10 min:

```
@reboot python /home/pi/gandi-dyndns.py
*/10 * * * * python /home/pi/gandi-dyndns.py
```

Finally reload the crontab.

```
sudo /etc/init.d/cron reload
```

This script is based on: https://github.com/matt1/gandi-ddns
