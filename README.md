# py_archivesmanager
<h2>Descrição:</h2>
<p>Um archive é um “arquivo de arquivos”; ou seja, é um arquivo que contém uma coleção de outros
arquivos, em uma estrutura que torna possível recuperar individualmente cada arquivo nele
armazenado [1]. Um arquivador (archiver) é um programa que permite criar e modificar archives, bem
como extrair arquivos de um archive.</p>
<p>Nesse contexto, a tarefa deste projeto é fazer um arquivador que funcione em modo texto (Prompt do
Windows ou terminal do Linux) e que implemente os seguintes casos de uso:
    – C1. Criar um archive com base em uma lista de arquivos informados.
    – C2. Inserir um arquivo em um archive já criado.
    – C3. Listar os nomes dos arquivos armazenados em um archive.
    – C4. Extrair um arquivo de um archive, dado o nome do arquivo (sem remover esse arquivo de dentro do archive).
    – C5. Remover um arquivo de um archive, dado o nome do arquivo.
</p>
<h3>Os comandos do arquivador devem ser:</h3>
<p>
<b>arquivador -c &lsaquo;novoarchive.arq&rsaquo; &lsaquo;arq1&rsaquo; &lsaquo;arq2&rsaquo; ...</b><br />
Cria arquivo novoarchive.arq cujos arquivos são arq1, arq2 etc.<br />
<i>Exemplo:
    arquivador -c eleicao2018.arq intencoes_dos_candidatos.txt discurso13.mp3 discurso17.mp3
</i>
</p> 
<p>
<b>arquivador -i &lsaquo;archive.arq&rsaquo; &lsaquo;arq&rsaquo;</b><br />
Insere arquivo arq em archive.arq.<br />
<i>Exemplo:
    arquivador -i eleicao2018.arq democracia.doc
</i>
</p>
<p>
<b>arquivador -l &lsaquo;archive.arq&rsaquo;</b><br />
Lista os nomes de arquivos que estão em archive.arq, um por linha<br />
<i>Exemplo:
    arquivador -l eleicao2018.arq
</i>
</p>  
<p>
<b>arquivador -e &lsaquo;archive.arq&rsaquo; &lsaquo;arq&rsaquo;</b><br />
Extrai arquivo arq de archive.arq, caso exista.<br />
<i>Exemplo:
    arquivador -e eleicao2018.arq intencoes_dos_candidatos.txt
</i>
</p>
<p>
<b>arquivador -r &lsaquo;archive.arq&rsaquo; &lsaquo;arq&rsaquo;</b><br />
Remove arquivo arq de archive.arq, caso exista.<br />
<i>Exemplo:
    arquivador -r eleicao2018.arq ditadura.doc
</i>
</p>
