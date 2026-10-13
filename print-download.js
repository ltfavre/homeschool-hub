// Self-contained, text-based Letter PDF export. No print dialog or popup required.
window.PrintDownload = (() => {
  const clean = value => String(value).replace(/[\u2018\u2019]/g,"'").replace(/[\u201c\u201d]/g,'"').replace(/[\u2013\u2014]/g,'-').replace(/\u2192/g,'->').replace(/\u2022/g,'-').replace(/\u2026/g,'...').replace(/\u00a0/g,' ').replace(/[^\x00-\xff]/g,'?');
  const escape = value => clean(value).replace(/[\\()]/g,'\\$&').replace(/[\x80-\xff]/g,c=>'\\'+c.charCodeAt(0).toString(8).padStart(3,'0'));
  function wrap(text, columns) {
    const lines=[];
    for (const paragraph of clean(text).split('\n')) {
      let line='';
      for(let word of paragraph.trim().split(/\s+/)) {
        if(line && line.length+word.length+1>columns){lines.push(line);line='';}
        while(word.length>columns){if(line){lines.push(line);line='';}lines.push(word.slice(0,columns));word=word.slice(columns);}
        if(word)line+=(line?' ':'')+word;
      }
      lines.push(line);
    }
    return lines;
  }
  function create(root, title) {
    const pages=[[]]; let y=748;
    const next=()=>{if(pages.at(-1).length){pages.push([]);y=748;}};
    const room=h=>{if(y-h<44)next();};
    function text(value,size=10,bold=false,gap=7) {
      const lines=wrap(value,Math.floor(528/(size*.6))),leading=size*1.4;
      room(Math.min(lines.length*leading+gap,704));
      for(const line of lines){room(leading);pages.at(-1).push(`BT /${bold?'F2':'F1'} ${size} Tf 42 ${y.toFixed(2)} Td (${escape(line)}) Tj ET`);y-=leading;}
      y-=gap;
    }
    function walk(el) {
      if(el.classList.contains('grade-packet')||el.classList.contains('print-subject')||el.classList.contains('print-section'))next();
      if(el.classList.contains('question')) {
        const p=el.querySelector('p'),space=el.querySelector('.work-space');
        const h=(p?wrap(p.textContent,88).length*14+7:0)+(space?parseFloat(space.style.minHeight)||36:0);
        room(Math.min(h,650));
      }
      if(el.classList.contains('work-space')){const h=Math.max(30,parseFloat(el.style.minHeight)||36);room(h);y-=h;pages.at(-1).push(`0.6 G 42 ${y.toFixed(2)} m 570 ${y.toFixed(2)} l S 0 G`);y-=10;return;}
      if(/^H[1-6]$/.test(el.tagName)){text(el.textContent,el.tagName==='H1'?15:el.tagName==='H2'?13:11,true);return;}
      if(el.tagName==='P'||el.classList.contains('response-lines')||el.classList.contains('source-url')||el.classList.contains('resource-meta')||el.classList.contains('resource-access')){text(el.textContent,el.classList.contains('metadata')||el.classList.contains('source-url')?9:10);return;}
      if(el.tagName==='A'){text(el.textContent,10,true);if(!el.parentElement.querySelector('.source-url'))text(el.href,9);return;}
      for(const child of el.childNodes){if(child.nodeType===1)walk(child);else if(child.nodeType===3&&child.textContent.trim())text(child.textContent.trim());}
    }
    walk(root);
    const objects=[null,'<< /Type /Catalog /Pages 2 0 R >>',null,'<< /Type /Font /Subtype /Type1 /BaseFont /Courier /Encoding /WinAnsiEncoding >>','<< /Type /Font /Subtype /Type1 /BaseFont /Courier-Bold /Encoding /WinAnsiEncoding >>'];
    const kids=[];
    pages.forEach((commands,i)=>{
      commands.push(`BT /F1 8 Tf 42 25 Td (VenvLearning | ${escape(title)} | Page ${i+1} of ${pages.length}) Tj ET`);
      const stream=commands.join('\n'),pageId=objects.length,streamId=pageId+1;kids.push(`${pageId} 0 R`);
      objects.push(`<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 3 0 R /F2 4 0 R >> >> /Contents ${streamId} 0 R >>`,`<< /Length ${stream.length} >>\nstream\n${stream}\nendstream`);
    });
    objects[2]=`<< /Type /Pages /Count ${pages.length} /Kids [${kids.join(' ')}] >>`;
    let pdf='%PDF-1.4\n',offsets=[0];
    for(let i=1;i<objects.length;i++){offsets.push(pdf.length);pdf+=`${i} 0 obj\n${objects[i]}\nendobj\n`;}
    const start=pdf.length;pdf+=`xref\n0 ${objects.length}\n0000000000 65535 f \n`+offsets.slice(1).map(o=>String(o).padStart(10,'0')+' 00000 n \n').join('')+`trailer\n<< /Size ${objects.length} /Root 1 0 R >>\nstartxref\n${start}\n%%EOF\n`;
    return new Blob([pdf],{type:'application/pdf'});
  }
  function prepare(anchor, root, filename) {
    if(anchor.dataset.pdfUrl)URL.revokeObjectURL(anchor.dataset.pdfUrl);
    const url=URL.createObjectURL(create(root,filename.replace(/\.pdf$/,'')));
    anchor.href=url;anchor.download=filename;anchor.dataset.pdfUrl=url;anchor.removeAttribute('aria-disabled');
  }
  return {create,prepare};
})();
