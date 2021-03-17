# tarefas-api
Uma rest API para gerenciamento de tarefas!, com essa API você consegue visualizar todas as tarefas mudar o status, também adicionar novas tarefas, editar e também excluir.

É necessário usar o programa Postman e também ter a biblioteca Flask instalada em seu sistema para utilizar a API por completo, também é necessário um conhecimento em python para poder entender como funciona toda a aplicação.

Método GET:

Utilizando o método GET você pode ver cara tarefa individualmente, utilizando o URI https://127.0.0.1:5000/tarefas/ e colocar o id da tarefa no final, exemplo:

http://127.0.0.1:5000/tarefas/0

![image](https://user-images.githubusercontent.com/48499123/111498246-8d0bdc00-8720-11eb-987a-269f0b2b2adf.png)

Você também pode ver todas as tarefas utilizando a URI sem definir o id no final.

![image](https://user-images.githubusercontent.com/48499123/111498486-c0e70180-8720-11eb-9cfc-0811c6f9c550.png)

Método POST:

Com o método POST você consegue adicionar tarefas na API, Basta selecionar o método POST no Postman, clicar em ``body`` > selecionar o modo ``raw`` > trocar de ``text`` pra ``json`` e adicionar uma nova tarefa, exemplo:

![image](https://user-images.githubusercontent.com/48499123/111498971-394dc280-8721-11eb-9397-30ca924b34ab.png)

Método PUT:

Com a API ainda é possivel trocar o status o status de tarefa, de ``pendente`` para ``concluído`` utilizando método PUT, fazendo o mesmo procedimento do POST no Postman, exemplo:

![image](https://user-images.githubusercontent.com/48499123/111499469-bf6a0900-8721-11eb-909a-ec359bd75ab5.png)

Método DELETE:

E também é possivel deletar tarefas com o método DELETE utliziando a URI com o id da tarefa pra ser excluida, exemplo:

http://127.0.0.1:5000/tarefas/2/

![image](https://user-images.githubusercontent.com/48499123/111499631-e7f20300-8721-11eb-8858-d83a1bf23438.png)
