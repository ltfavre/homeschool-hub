(() => {
  const $ = id => document.getElementById(id);
  async function api(body) {
    const response = await fetch('/api/family/home-assistant-token', body ? {method:'POST', headers:{'content-type':'application/json'}, body:JSON.stringify(body)} : {});
    const result = await response.json(); if (!response.ok) throw Error(result.error || 'Connection unavailable'); return result;
  }
  async function refresh() {
    const {connections} = await api();
    $('connections').replaceChildren();
    for (const connection of connections) {
      const row = document.createElement('p'), button = document.createElement('button'); button.className='secondary lms-small';
      row.append(document.createTextNode(`Connected ${new Date(connection.created_at*1000).toLocaleDateString('en-US',{month:'short',day:'numeric',year:'numeric'})} `));
      button.textContent = 'Disconnect'; button.onclick = async () => {try {await api({action:'revoke',id:connection.id}); await refresh(); $('status').textContent='Connection revoked.';} catch(error){$('status').textContent=error.message;}};
      row.append(button); $('connections').append(row);
    }
    if (!connections.length) $('connections').textContent='No active school connections.';
  }
  $('create').onclick = async () => {
    $('create').disabled = true;
    try {const result=await api({action:'create'}); $('token').textContent=result.token; $('newKey').hidden=false; await refresh(); $('status').textContent='Key ready. Add it to Home Assistant.';}
    catch(error){$('status').textContent=error.message;}
    finally{$('create').disabled=false;}
  };
  (async()=>{try {await refresh(); $('create').disabled=false; $('status').textContent='Ready to connect.';} catch(error){$('status').textContent=error.message;}})();
})();
