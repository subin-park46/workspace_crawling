def today():
    service_key = "QVIUn7pKNXN2sDdtDlLPgW6o5%2BC53oMWpIKgpkbdGGRpqTI59QX%2F%2Fl6tsUfB4DvYCNESmgAJfE4uUPtiO5LjrA%3D%3D"
    url = f"http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?ServiceKey={service_key}"
    print(url)

if __name__ == '__main__':
    today()