// Self-contained, text-based Letter PDF export. No print dialog or popup required.
window.PrintDownload = (() => {
  const clean = value => String(value).replace(/[\u2018\u2019]/g,"'").replace(/[\u201c\u201d]/g,'"').replace(/[\u2013\u2014]/g,'-').replace(/\u2192/g,'->').replace(/\u2022/g,'-').replace(/\u2026/g,'...').replace(/\u00a0/g,' ').replace(/[^\x00-\xff]/g,'?');
  const escape = value => clean(value).replace(/[\\()]/g,'\\$&').replace(/[\x80-\xff]/g,c=>'\\'+c.charCodeAt(0).toString(8).padStart(3,'0'));
  const widths=[[761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 278, 278, 355, 556, 556, 889, 667, 191, 333, 333, 389, 584, 278, 333, 278, 278, 556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 278, 278, 584, 584, 584, 556, 1015, 667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833, 722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 278, 278, 278, 469, 556, 333, 556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222, 833, 556, 556, 556, 556, 333, 500, 278, 556, 500, 722, 500, 500, 500, 334, 260, 334, 584, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 278, 333, 556, 556, 556, 556, 260, 556, 333, 737, 370, 556, 584, 333, 737, 333, 400, 584, 333, 333, 333, 556, 537, 278, 333, 333, 365, 556, 834, 834, 834, 611, 667, 667, 667, 667, 667, 667, 1000, 722, 667, 667, 667, 667, 278, 278, 278, 278, 722, 722, 778, 778, 778, 778, 778, 584, 778, 722, 722, 722, 722, 667, 667, 611, 556, 556, 556, 556, 556, 556, 889, 500, 556, 556, 556, 556, 278, 278, 278, 278, 556, 556, 556, 556, 556, 556, 556, 584, 611, 556, 556, 556, 556, 500, 556, 500], [761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 278, 333, 474, 556, 556, 889, 722, 238, 333, 333, 389, 584, 278, 333, 278, 278, 556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 333, 333, 584, 584, 584, 611, 975, 722, 722, 722, 722, 667, 611, 778, 722, 278, 556, 722, 611, 833, 722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 333, 278, 333, 584, 556, 333, 556, 611, 556, 611, 556, 333, 611, 611, 278, 278, 556, 278, 889, 611, 611, 611, 611, 389, 556, 333, 611, 556, 778, 556, 556, 500, 389, 280, 389, 584, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 761, 278, 333, 556, 556, 556, 556, 280, 556, 333, 737, 370, 556, 584, 333, 737, 333, 400, 584, 333, 333, 333, 611, 556, 278, 333, 333, 365, 556, 834, 834, 834, 611, 722, 722, 722, 722, 722, 722, 1000, 722, 667, 667, 667, 667, 278, 278, 278, 278, 722, 722, 778, 778, 778, 778, 778, 584, 778, 722, 722, 722, 722, 667, 667, 611, 556, 556, 556, 556, 556, 556, 889, 556, 556, 556, 556, 556, 278, 278, 278, 278, 611, 611, 611, 611, 611, 611, 611, 584, 611, 611, 611, 611, 611, 556, 611, 556]];
  const measure=(text,size,bold=false)=>Array.from(clean(text)).reduce((sum,c)=>sum+(widths[bold?1:0][c.charCodeAt(0)]||600),0)*size/1000;
  function wrap(text, width=528, size=11, bold=false) {
    const lines=[];
    for(const paragraph of clean(text).split('\n')) {
      let line='';
      for(let word of paragraph.trim().split(/\s+/)) {
        if(line&&measure(line+' '+word,size,bold)>width){lines.push(line);line='';}
        while(measure(word,size,bold)>width){let n=1;while(n<word.length&&measure(word.slice(0,n+1),size,bold)<=width)n++;lines.push(word.slice(0,n));word=word.slice(n);}
        if(word)line+=(line?' ':'')+word;
      }
      lines.push(line);
    }
    return lines;
  }
  function create(root, title) {
    const pages=[[]],links=[[]]; let y=748;
    const next=()=>{if(pages.at(-1).length){pages.push([]);links.push([]);y=748;}};
    const room=h=>{if(y-h<44)next();};
    function text(value,size=11,bold=false,gap=10,href=null) {
      const lines=wrap(value,528,size,bold),leading=size*1.55;
      room(Math.min(lines.length*leading+gap,704));
      for(const line of lines){room(leading);if(href){const width=measure(line,size,bold);links.at(-1).push({href,rect:[42,y-3,42+width,y+size]});pages.at(-1).push(`0.12 0.32 0.46 rg 0.12 0.32 0.46 RG 42 ${y-2} m ${42+width} ${y-2} l S`);}pages.at(-1).push(`BT /${bold?'F2':'F1'} ${size} Tf 42 ${y.toFixed(2)} Td (${escape(line)}) Tj ET`);y-=leading;if(href)pages.at(-1).push("0 g 0 G");}
      y-=gap;
    }
    function walk(el) {
      if(el.classList.contains('grade-packet')||el.classList.contains('print-subject')||el.classList.contains('print-section'))next();
      if(el.classList.contains('question')) {
        const p=el.querySelector('p'),space=el.querySelector('.work-space');
        const h=(p?wrap(p.textContent,528,11).length*17.05+10:0)+(space?parseFloat(space.style.minHeight)||36:0);
        room(Math.min(h,650));
      }
      if(el.classList.contains('work-space')){const h=Math.max(30,parseFloat(el.style.minHeight)||36);room(h);y-=h;pages.at(-1).push(`0.6 G 42 ${y.toFixed(2)} m 570 ${y.toFixed(2)} l S 0 G`);y-=10;return;}
      if(/^H[1-6]$/.test(el.tagName)){text(el.textContent,el.tagName==='H1'?20:el.tagName==='H2'?16:13,true);return;}
      if(el.classList.contains('source-url'))return;
      if(el.tagName==='P'||el.classList.contains('response-lines')||el.classList.contains('source-url')||el.classList.contains('resource-meta')||el.classList.contains('resource-access')){text(el.textContent,el.classList.contains('metadata')||el.classList.contains('source-url')?10:11);return;}
      if(el.tagName==='A'){text(el.textContent+'  [Open link]',11,true,6,el.href);try{text(new URL(el.href).hostname,9,false,12);}catch{}return;}
      for(const child of el.childNodes){if(child.nodeType===1)walk(child);else if(child.nodeType===3&&child.textContent.trim())text(child.textContent.trim());}
    }
    walk(root);
    const objects=[null,'<< /Type /Catalog /Pages 2 0 R >>',null,'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>','<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>'];
    const kids=[];
    pages.forEach((commands,i)=>{
      commands.push(`BT /F1 8 Tf 42 25 Td (VenvLearning | ${escape(title)} | Page ${i+1} of ${pages.length}) Tj ET`);
      const annotationIds=links[i].map(link=>{const id=objects.length;objects.push(`<< /Type /Annot /Subtype /Link /Rect [${link.rect.join(' ')}] /Border [0 0 0] /A << /S /URI /URI (${escape(link.href)}) >> >>`);return id+' 0 R';});
      const stream=commands.join('\n'),pageId=objects.length,streamId=pageId+1;kids.push(`${pageId} 0 R`);
      objects.push(`<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 3 0 R /F2 4 0 R >> >> /Contents ${streamId} 0 R /Annots [${annotationIds.join(' ')}] >>`,`<< /Length ${stream.length} >>\nstream\n${stream}\nendstream`);
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
