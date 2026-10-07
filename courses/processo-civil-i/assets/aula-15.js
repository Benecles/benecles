(function(){
  var claim=document.getElementById('claim'),status=document.getElementById('status'),method=document.getElementById('method'),result=document.getElementById('result');
  if(!claim||!status||!method||!result)return;
  function update(){
    var c=claim.value,s=status.value,m=method.value;
    var text='';
    if(m==='records'){
      if(c==='attempts') text='A decisão registra a alegação na impugnação e pergunta se ela constava da inicial. As peças permitem conferir onde foi feita; o excerto não aponta um meio para provar a ocorrência das tentativas.';
      else if(c==='purchase') text='A decisão menciona a compra em novembro de 2012. As peças dos autos podem ser consultadas para localizar a afirmação; o excerto não informa uma categoria do art. 374 aplicável a essa data.';
      else text='A decisão informa o ajuizamento em 18 de agosto de 2015. As peças podem mostrar onde a data aparece; o excerto não informa uma categoria do art. 374 aplicável a essa data.';
    } else if(m==='none'){
      text=c==='attempts'?'O excerto não indica meio para provar se as tentativas ocorreram. Sem meio proposto, não há base para uma decisão concreta de admissibilidade pelos arts. 369–370.':'A opção selecionada não corresponde ao uso descrito no registro: as peças são meios para conferir seu conteúdo. O status da afirmação quanto ao art. 374 permanece a verificar.';
    } else {
      text='A falta de especificação no Código não decide sozinha a admissibilidade. O art. 369 exige meio legal e moralmente legítimo, ligado à afirmação relevante; o art. 370 permite indeferir, com fundamentação, diligência inútil ou meramente protelatória.';
    }
    if(s==='374') text+=' O excerto não informa que a afirmação se enquadre em uma das quatro categorias do art. 374; não é possível atribuir essa condição a partir desses dados.';
    else if(s==='asserted') text+=' O status “alegação localizada” diz respeito à presença da afirmação na peça, não à ocorrência do evento descrito.';
    result.innerHTML='<span class="result-label">Resultado.</span> '+text;
  }
  [claim,status,method].forEach(function(el){el.addEventListener('change',update)});
})();
