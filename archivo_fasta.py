from Bio import SeqIO

def codons(frame, secuencia, output_handle):
    with open(output_handle, "w") as out_handle:
        for record in SeqIO.parse(secuencia, "fasta"):
            sequence = str(record.seq[frame:])
            codons = [sequence[i:i+3] for i in range(0, len(sequence), 3) if len(sequence[i:i+3]) ==3]
            codons_str = " ".join(codons)
            out_handle.write(f">{record.id}_frame{frame+1}\n{codons_str}\n")

#Archivo Fasta de entrada
archivo_fasta = "/Users/frida_galan/Desktop/PythonSEM2/Notes/seq.nt.fa"           

# Llamar a la función para cada uno de los 6 marcos de lectura
for frame in range(3):
    codons(frame, archivo_fasta, f"/Users/frida_galan/Desktop/PythonSEM2/Notes/Frame{frame+1}.fasta")
    codons(frame, archivo_fasta, f"/Users/frida_galan/Desktop/PythonSEM2/Notes/Frame{frame+4}.fasta")

