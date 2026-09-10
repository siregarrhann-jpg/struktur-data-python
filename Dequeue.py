class Queue:
    def __init__(self):
        self.items=[]
    
    def enqueue(self,Data):
        self.items.append(Data)
        
    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(1)
        else:
            return "Antrean kosong!"
        
antrean = Queue()
antrean.enqueue("farhan")
antrean.enqueue("zaki")  
antrean.enqueue("sayyid")
antrean.enqueue("anfasa")
antrean.enqueue("sultan")
print("antrean Awal" ,antrean.items)

yang_keluar = antrean.dequeue()
print("Data yang keluar:", yang_keluar)
print("Antrean Sekarang:", antrean.items)