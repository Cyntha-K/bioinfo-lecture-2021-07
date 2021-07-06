import sys
import gzip
 
class FastaReader:
    def __init__(self):
        self.fastaFile = ""
        self.count = 0
 
    def readFasta(self):
        with gzip.open(self.fastaFile,'rb') as fr:
            for line in fr:
                s = line.decode("utf-8").strip()
                if not s.startswith(">"):
                    self.count += len(s)
  
class Fastacounter:
    def __init__(self):
        self.fastaFile = ""
        self.count = 0
   
    def count_nucleotide(self):
        with gzip.open(self.fastaFile, 'rb') as fr:
            for line in fr:
                r = line.decode("utf-8").strip()
                if not s.stratswith(">"):
                    self.count('A') += len(r)
                    self.count('T') += len(r)
                    self.count('G') += len(r)
                    self.count('C') += len(r)

 
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("#usage: python %s <fasta.gz>" %sys.argv[0])
        sys.exit()

    fastaFile = sys.argv[1]
    fastaReader = FastaReader()
    fastaCounter = FastaCounter()
    fastaReader.fastaFile = fastaFile1
    fastaCounter.fastaFile = fastaFile2
    fastaReader.readFasta()
    fastaCounter.count_nucleotide()

    print(fastaReader.count)
    print(fastaReader.readFasta())
    print(fastaCounter.count_nucleotide())



