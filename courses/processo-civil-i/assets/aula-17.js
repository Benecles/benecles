(function(){
  var form=document.getElementById('a17-controls');
  if(!form)return;
  var result=document.getElementById('a17-result');
  var title=result.querySelector('.a17-result__title');
  var note=result.querySelector('.a17-result__text');
  function update(){
    var fact=form.elements.fato.value;
    var holder=fact==='constitutivo'?'autor':'réu';
    var basis=form.elements.hipotese.value;
    var reasoned=form.elements.fundamentada.checked;
    var opportunity=form.elements.oportunidade.checked;
    var feasible=form.elements.cumprivel.value;
    result.dataset.state='default';
    if(basis==='nenhuma'){
      title.textContent='Mantém-se a regra do caput';
      note.textContent='O ônus ordinário cabe ao '+holder+' para este fato.';
      return;
    }
    if(feasible==='nao'){
      result.dataset.state='blocked';
      title.textContent='Transferência vedada pelo § 2º';
      note.textContent='O encargo que a parte receberia seria impossível ou excessivamente difícil de cumprir.';
      return;
    }
    if(!reasoned||!opportunity){
      title.textContent='Mantém-se a regra do caput';
      note.textContent='O § 1º exige decisão fundamentada e oportunidade para a parte se desincumbir do encargo.';
      return;
    }
    result.dataset.state='redistributed';
    title.textContent='Redistribuição fundamentada com oportunidade';
    note.textContent='A nova atribuição depende da hipótese selecionada, da razão exposta e da chance de produzir a prova.';
  }
  form.addEventListener('change',update);
  update();
})();
