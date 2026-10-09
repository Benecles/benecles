(function(){
  var form=document.getElementById('a03-questions');
  if(!form)return;
  var result=document.getElementById('a03-result');
  var combinations={
    'necessaria-unitario':['a03-nu','Litisconsórcio necessário e unitário. Todos devem participar, e o mérito deve ser decidido de modo uniforme.'],
    'necessaria-simples':['a03-ns','Litisconsórcio necessário e simples. Todos devem participar, embora o mérito possa ser decidido de modo diferente para cada um.'],
    'facultativa-unitario':['a03-fu','Litisconsórcio facultativo e unitário. A reunião é opcional, mas o mérito deve ser decidido de modo uniforme.'],
    'facultativa-simples':['a03-fs','Litisconsórcio facultativo e simples. A reunião é opcional, e o mérito pode ser decidido de modo diferente para cada um.']
  };
  function update(){
    var participacao=form.elements.participacao.value;
    var uniformidade=form.elements.uniformidade.value;
    document.querySelectorAll('#a03-classifier td[data-combination]').forEach(function(cell){cell.removeAttribute('aria-current')});
    if(!participacao||!uniformidade){
      result.textContent='Escolha uma resposta em cada pergunta para localizar a combinação.';
      return;
    }
    var key=participacao+'-'+uniformidade;
    var item=combinations[key];
    document.getElementById(item[0]).setAttribute('aria-current','true');
    result.textContent=item[1]+' (CPC, arts. 114–116).';
  }
  form.addEventListener('change',update);
  update();
})();
