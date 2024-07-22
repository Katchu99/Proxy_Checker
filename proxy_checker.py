import requests
from requests.exceptions import ProxyError, ConnectTimeout
import socks
import socket
from multiprocessing import Pool
import os

# List of proxies
proxies = []

#List of working proxies
working_proxies = []


# Function to check http proxy
def check_http_proxy(proxy):
    proxy_url = f"{proxy['type']}://{proxy['host']}:{proxy['port']}"
    proxies_dict = {
        "http": proxy_url,
        "https": proxy_url
    }
    try:
        response = requests.get('https://httpbin.org/ip', proxies=proxies_dict, timeout=5)
        if response.status_code == 200:
            print(f"Process {os.getpid()}: HTTP Proxy works: {proxy_url}")
            return proxy
        else:
            print(f"Process {os.getpid()}: HTTP Proxy does not work: {proxy_url}")
            return None
    except (ProxyError, ConnectTimeout) as e:
        print(f"Process {os.getpid()}: HTTP Proxy does not work: {proxy_url}") # \n Error: {e}")
        return None

# Function to check socks proxy
def check_socks_proxy(proxy):
    socks_type = socks.SOCKS4 if proxy["type"] == "socks4" else socks.SOCKS5
    socks.set_default_proxy(socks_type, proxy["host"], proxy["port"])
    socket.socket = socks.socksocket
    try:
        response = requests.get('https://httpbin.org/ip', timeout=5)
        if response.status_code == 200:
            print(f"Process {os.getpid()}: SOCKS Proxy works: {proxy['type']}://{proxy['host']}:{proxy['port']}")
            return proxy
        else:
            print(f"Process {os.getpid()}: SOCKS Proxy does not work: {proxy['type']}://{proxy['host']}:{proxy['port']}")
            return None
    except (ProxyError, ConnectTimeout, socks.ProxyConnectionError, socket.timeout, socket.error) as e:
        print(f"Process {os.getpid()}: SOCKS Proxy does not work: {proxy['type']}://{proxy['host']}:{proxy['port']}") # \n Error: {e}")
        return None

# Check all proxies in the list
def check_proxy(proxy):
    print(f"Process {os.getpid()}: Checking proxy: {proxy['host']}")
    if proxy["type"] in ["http", "https"]:
        return check_http_proxy(proxy)
    elif proxy["type"] in ["socks4", "socks5"]:
        return check_socks_proxy(proxy)
    else:
        print(f"Process {os.getpid()}: Proxy type does not match, Proxy: {proxy}")

def main():
    # Read proxies from proxies.txt
    with open("proxies.txt", "r") as proxies_txt:
        for p in proxies_txt:
            if "#" in p:
                continue
            else:
                type = p.split(" ")[0]
                host = p.split(" ")[1]
                port = int(p.split(" ")[2].replace("\n",""))
                
                proxies.append({"type": type, "host": host, "port": port})

    # Use multiprocessing to check proxies
    with Pool(processes=4) as pool:
        results = pool.map(check_proxy, proxies)

    # Filter out None values and write working proxies to file
    global working_proxies
    working_proxies = [proxy for proxy in results if proxy is not None]

    with open("working_proxies.txt", "w+") as working_proxies_txt:
        for proxy in working_proxies:
            working_proxies_txt.write(f"{proxy['type']} {proxy['host']} {proxy['port']}\n")

if __name__ == "__main__":
    main()