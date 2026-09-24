<?php
function definirPrioridade(int $dia = 0){
    if ($dia <= 3)
        echo "Baixa";
    elseif ($dia >= 4)
        echo "Média";
    elseif ($dia <= 7)
        echo "Média";
    else
        echo "Alta";
}
definirPrioridade (2);
