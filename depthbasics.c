void AlgobasicoRitmo(){

	int menorCusto = MAX_INT;
	char melhorCaminho = "";
	insere(origem, 0);

	while(pilha){
		x = remove();
		if(x.caminho == Destino){
			if(x.custo < menorCusto){

				menorCusto = x.custo;
				melhorCaminho = x.caminho;
			}
		}
		else{
		    for cada vértice adjacente ao atual
			    insere(Vi, x.custo + custo do enlace);
		}
		printf(melhorCaminho, menorCusto);
	}
}
