import pandas as pd
# import codecs

class Data:
    
    urls = [
        'https://en.wikipedia.org/wiki/Sandy_Bridge',
        'https://en.wikipedia.org/wiki/Ivy_Bridge_(microarchitecture)',
        'https://en.wikipedia.org/wiki/Haswell_(microarchitecture)',
        'https://en.wikipedia.org/wiki/Broadwell_(microarchitecture)',
        'https://en.wikipedia.org/wiki/Skylake_(microarchitecture)',
        'https://en.wikipedia.org/wiki/Kaby_Lake',
        'https://en.wikipedia.org/wiki/Coffee_Lake',
        'https://en.wikipedia.org/wiki/Comet_Lake_(microprocessor)'
    ]
    
    def csvFilePath(self, gen):
        return f'./intel_gen_{gen}.csv'
    
    def getData(self, indexUrl, indexTable, gen):
        try:
            dfs = pd.read_html(self.urls[indexUrl])
            # pd.DataFrame(dfs.to_records())
            # selectedTable = dfs[indexTable]
            # selectedTable.columns = selectedTable.droplevel('Targetsegment')
            # cleanDf = pd(dfs[indexTable].to_records())
            # dfs.columns = dfs.columns.get_level_values(0)
            # dfs[indexTable].to_json(f'./intel_gen_{gen}.json', orient='table')
            # selectedTable.to_json(f'./intel_gen_{gen}.json', orient='table')
            dfs[indexTable].to_csv(self.csvFilePath(gen), encoding='utf-8-sig', index=False)
            # codecs.open(self.csvFilePath(gen), 'r', encoding='ascii', errors='ignore')
        except Exception as e:
            print(f'error in gen-{gen}: {e}')
            # dfs[indexTable].to_json(f'./intel_gen_{gen}.json')
    # for url in urls:
    #     dfs = pd.read_html('url')

    def getCompleteData(self):
        self.getData(0,3,2)
        self.getData(1,9,3)
        self.getData(2,2,4)
        self.getData(4,2,6)
        self.getData(5,1,7)
        self.getData(6,1,8)
        self.getData(6,4,9)
        self.getData(7,1,10)