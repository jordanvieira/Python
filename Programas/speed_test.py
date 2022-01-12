import speedtest

test = speedtest.Speedtest()


print("Testando download")
down = test.download()
rsDown = round(down)
fDown = int(rsDown / 1e+6)

print("Testando Upload\n")
upload = test.download()
rsUp = round(upload)
fUp = int(rsUp / 1e+6)


print(f"Sua velocidade de download é de: {fDown} mb/s")
print(f"Sua velocidade de upload é de: {fUp} mb/s")
