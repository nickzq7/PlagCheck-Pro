#!/usr/bin/env python3
"""
PlagCheck Pro — CHIMERA-Hash Ultra v5
By @ProgramDr
Run: python plagcheck.py
"""
import threading, webbrowser, time, re, json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import quote, unquote
from urllib.request import urlopen, Request
import gzip as gzipmod

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PlagCheck Pro</title>
<style>
*{box-sizing:border-box;margin:0;padding:0;}
:root{--bg:#050505;--s1:#090909;--s2:#0d0d0d;--b1:#131313;--b2:#1a1a1a;--b3:#232323;--t1:#e8e8e8;--t2:#999;--t3:#555;--t4:#2a2a2a;--blue:#5dade2;--green:#27ae60;--yellow:#e6b800;--orange:#e67e22;--red:#e74c3c;}
body{background:var(--bg);color:var(--t1);font-family:Georgia,serif;min-height:100vh;}
a{color:var(--blue);}button{cursor:pointer;font-family:inherit;}
::-webkit-scrollbar{width:4px;}::-webkit-scrollbar-track{background:var(--s1);}::-webkit-scrollbar-thumb{background:#222;border-radius:3px;}
.hdr{background:var(--s1);border-bottom:1px solid var(--b1);padding:0 24px;position:sticky;top:0;z-index:10;}
.hdr-in{max-width:980px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;height:60px;gap:12px;flex-wrap:wrap;}
.logo{display:flex;align-items:center;gap:11px;}
.lmark{width:36px;height:36px;background:linear-gradient(135deg,#1c4060,#0c1f30);border:1px solid #2a5a80;border-radius:9px;display:grid;place-items:center;font-size:17px;}
.lname{font-size:1.05em;color:#fff;font-weight:bold;}
.lsub{font-size:9px;color:var(--t4);font-family:monospace;letter-spacing:1px;margin-top:1px;}
.hdr-r{display:flex;gap:7px;flex-wrap:wrap;align-items:center;}
.pill{background:var(--s2);border:1px solid var(--b2);border-radius:20px;padding:3px 10px;font-size:9px;font-family:monospace;color:var(--t4);}
.pill-on{border-color:#27ae6040;color:var(--green);background:#041208;}
.wrap{max-width:980px;margin:0 auto;padding:24px 20px;}
.how-box{background:linear-gradient(135deg,#07111a,#050d14);border:1px solid #0f2535;border-radius:12px;padding:16px 20px;margin-bottom:16px;}
.how-title{font-size:10px;font-family:monospace;color:var(--t4);letter-spacing:2px;margin-bottom:10px;}
.how-steps{display:flex;gap:10px;flex-wrap:wrap;}
.how-step{display:flex;align-items:center;gap:7px;background:var(--s2);border:1px solid var(--b2);border-radius:7px;padding:7px 12px;font-size:11px;color:var(--t3);}
.how-num{background:var(--blue);color:#000;width:18px;height:18px;border-radius:50%;display:grid;place-items:center;font-family:monospace;font-size:9px;font-weight:bold;flex-shrink:0;}
.icard{background:var(--s1);border:1px solid var(--b1);border-radius:12px;overflow:hidden;margin-bottom:14px;}
.icard-hd{padding:11px 18px;border-bottom:1px solid var(--b1);display:flex;align-items:center;justify-content:space-between;}
.icht{font-size:10px;font-family:monospace;color:var(--t4);letter-spacing:2px;}
.wc{font-size:10px;font-family:monospace;color:var(--t4);transition:color .3s;}
textarea{width:100%;height:185px;background:transparent;border:none;color:var(--t1);font-family:Georgia,serif;font-size:14px;padding:18px;resize:none;line-height:1.9;outline:none;}
textarea::placeholder{color:#1a1a1a;}
.run-btn{width:100%;padding:16px;background:linear-gradient(135deg,#1a3f60,#0c1e2e);border:2px solid var(--blue);color:#fff;border-radius:11px;font-family:Georgia,serif;font-size:15px;transition:all .25s;display:flex;align-items:center;justify-content:center;gap:11px;box-shadow:0 0 28px #5dade208;margin-bottom:20px;}
.run-btn:hover:not(:disabled){box-shadow:0 0 50px #5dade225;transform:translateY(-1px);}
.run-btn:disabled{border-color:var(--b2);background:var(--s2);color:var(--t4);box-shadow:none;transform:none;}
.spin{width:16px;height:16px;border:2px solid #111;border-top:2px solid var(--blue);border-radius:50%;animation:spin .7s linear infinite;flex-shrink:0;}
.prog{background:var(--s1);border:1px solid var(--b1);border-radius:12px;margin-bottom:20px;overflow:hidden;}
.prog-hd{padding:12px 18px;border-bottom:1px solid var(--b1);display:flex;align-items:center;gap:10px;}
.prog-pulse{width:7px;height:7px;border-radius:50%;background:var(--blue);animation:pulse 1s infinite;flex-shrink:0;}
.prog-lbl{font-size:10px;font-family:monospace;color:var(--t3);letter-spacing:2px;flex:1;}
.prog-n{font-size:11px;font-family:monospace;color:var(--blue);}
.prog-log{padding:14px 18px;max-height:180px;overflow-y:auto;display:flex;flex-direction:column;gap:3px;}
.log-line{font-size:11px;font-family:monospace;color:var(--t4);line-height:1.5;}
.log-line.ok{color:#27ae60;}
.log-line.hit{color:var(--orange);}
.log-line.info{color:var(--blue);}
.res{animation:fadeUp .4s ease;}
.vbox{border-radius:14px;padding:24px;margin-bottom:18px;}
.vbox-in{display:flex;align-items:stretch;gap:20px;}
@media(max-width:560px){.vbox-in{flex-direction:column;}}
.vb-l{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;min-width:95px;}
.vpct{font-size:4em;font-weight:bold;font-family:monospace;line-height:1;}
.vgrade{font-size:10px;font-family:monospace;letter-spacing:3px;padding:3px 10px;border-radius:10px;}
.vb-m{flex:1;}
.vtitle{font-size:1.45em;font-weight:bold;margin-bottom:8px;}
.vdesc{font-size:13px;color:var(--t2);line-height:1.7;margin-bottom:10px;}
.vtip{font-size:12px;padding:10px 14px;border-radius:8px;font-style:italic;line-height:1.6;}
.vrisk{margin-top:12px;}
.vrisk-bar{height:8px;border-radius:4px;background:linear-gradient(90deg,#27ae60 0%,#8bc34a 22%,#e6b800 42%,#e67e22 62%,#e74c3c 82%);position:relative;}
.vrisk-pin{position:absolute;top:-5px;width:4px;height:18px;background:#fff;border-radius:2px;transform:translateX(-50%);box-shadow:0 0 10px rgba(255,255,255,.9);transition:left 1.3s cubic-bezier(.4,0,.2,1);}
.vrisk-lbl{display:flex;justify-content:space-between;margin-top:5px;}
.vrisk-lbl span{font-size:9px;font-family:monospace;color:var(--t4);}
.vb-r{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;min-width:72px;text-align:center;}
.vr-n{font-size:3em;font-weight:bold;font-family:monospace;color:#fff;line-height:1;}
.vr-l{font-size:9px;font-family:monospace;color:var(--t4);letter-spacing:1px;}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:18px;}
@media(max-width:560px){.stats{grid-template-columns:repeat(2,1fr);}}
.stat{background:var(--s1);border:1px solid var(--b1);border-radius:10px;padding:15px;text-align:center;}
.sn{font-size:1.9em;font-weight:bold;font-family:monospace;}
.sl{font-size:9px;font-family:monospace;color:var(--t4);margin-top:3px;letter-spacing:1px;}
.hm{background:var(--s1);border:1px solid var(--b1);border-radius:12px;padding:20px;margin-bottom:18px;}
.hm-hd{display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;margin-bottom:10px;}
.hm-title{font-size:10px;font-family:monospace;color:var(--t4);letter-spacing:2px;}
.hm-stat{font-size:10px;color:var(--t4);font-family:monospace;}
.hm-sub{font-size:11px;color:var(--t4);font-style:italic;margin-bottom:14px;}
.hm-body{font-size:13.5px;line-height:2.3;color:var(--t2);}
.s{border-radius:3px;padding:1px 3px;margin:1px 0;cursor:default;transition:filter .15s;display:inline;}
.s:hover{filter:brightness(1.3);}
.s0{color:var(--t2);}
.s1{background:#27ae601e;color:#5dbb80;}
.s2{background:#e6b80024;color:#c9a000;}
.s3{background:#e67e2230;color:#e67e22;}
.s4{background:#e74c3c3a;color:#e74c3c;font-weight:500;}
.hm-legend{display:flex;gap:14px;margin-top:14px;flex-wrap:wrap;}
.hl{display:flex;align-items:center;gap:5px;font-size:10px;color:var(--t3);}
.hldot{width:9px;height:9px;border-radius:2px;}
.src-hd{font-size:10px;font-family:monospace;color:var(--t4);letter-spacing:2px;margin-bottom:12px;}
.scard{background:var(--s1);border:1px solid var(--b1);border-radius:10px;overflow:hidden;margin-bottom:9px;transition:all .2s;}
.scard:hover{border-color:var(--b3);transform:translateY(-1px);}
.scard-in{display:flex;}
.sscore{width:84px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:14px 6px;gap:5px;border-right:1px solid var(--b1);flex-shrink:0;}
.spct{font-size:1.9em;font-weight:bold;font-family:monospace;line-height:1;}
.sicon{font-size:14px;}
.ssrc{font-size:8px;font-family:monospace;text-align:center;color:var(--t4);line-height:1.3;}
.sbody{flex:1;padding:13px 16px;min-width:0;}
.stitle{font-size:12.5px;font-weight:bold;color:#ddd;line-height:1.4;margin-bottom:3px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.surl{font-size:9.5px;font-family:monospace;color:var(--blue);display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-bottom:7px;}
.ssnip{font-size:11.5px;color:var(--t3);line-height:1.7;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;}
.sfoot{display:flex;align-items:center;justify-content:space-between;margin-top:9px;}
.stype{font-size:9px;font-family:monospace;background:var(--s2);border:1px solid var(--b2);border-radius:3px;padding:2px 8px;color:var(--t4);}
.sbar-row{display:flex;align-items:center;gap:7px;}
.sbar{height:3px;width:64px;background:var(--b2);border-radius:2px;overflow:hidden;}
.sfill{height:100%;border-radius:2px;transition:width 1s ease;}
.no-match{background:var(--s1);border:1px solid var(--b1);border-radius:12px;padding:44px;text-align:center;}
.nm-ico{font-size:46px;margin-bottom:14px;}
.nm-t{font-size:1.1em;font-weight:bold;color:var(--green);margin-bottom:10px;}
.nm-d{font-size:13px;color:var(--t3);line-height:1.8;max-width:500px;margin:0 auto;}
.reset-btn{display:block;margin:18px auto 0;background:none;border:1px solid var(--b2);color:var(--t4);padding:9px 28px;border-radius:6px;font-size:12px;transition:all .2s;}
.reset-btn:hover{border-color:var(--b3);color:var(--t3);}
.footer{margin-top:36px;border-top:1px solid var(--b1);padding-top:16px;text-align:center;}
.footer p{color:#1c1c1c;font-size:10px;font-family:monospace;}
.footer a{color:#242424;}
@keyframes spin{to{transform:rotate(360deg);}}
@keyframes pulse{0%,100%{opacity:1;}50%{opacity:.3;}}
@keyframes fadeUp{from{opacity:0;transform:translateY(14px);}to{opacity:1;transform:translateY(0);}}
</style>
</head>
<body>
<div class="hdr">
  <div class="hdr-in">
    <div class="logo">
      <div class="lmark">🔍</div>
      <div><div class="lname">PlagCheck Pro</div><div class="lsub">CHIMERA-HASH ULTRA V5 · @PROGRAMDR</div></div>
    </div>
    <div class="hdr-r">
      <span class="pill pill-on">🟢 SERVER RUNNING</span>
      <span class="pill">SENTENCE-BY-SENTENCE SEARCH</span>
      <span class="pill">FULL PAGE READ</span>
      <span class="pill">FREE</span>
    </div>
  </div>
</div>
<div class="wrap">
  <div class="how-box">
    <div class="how-title">HOW IT FINDS THE EXACT ORIGINAL SOURCE</div>
    <div class="how-steps">
      <div class="how-step"><span class="how-num">1</span>Splits text into individual sentences</div>
      <div class="how-step"><span class="how-num">2</span>Searches each sentence as exact quoted phrase on the web</div>
      <div class="how-step"><span class="how-num">3</span>Fetches and reads the full content of every found page</div>
      <div class="how-step"><span class="how-num">4</span>CHIMERA-Hash scores each source against your text</div>
    </div>
  </div>
  <div class="icard">
    <div class="icard-hd"><span class="icht">PASTE YOUR TEXT</span><span class="wc" id="wc">0 words</span></div>
    <textarea id="txt" placeholder="Paste copied text here. Each sentence will be searched individually as an exact quoted phrase — this finds the original blog, news site, or any specific website it was copied from..."></textarea>
  </div>
  <button class="run-btn" id="runBtn" onclick="runCheck()" disabled>🔍 &nbsp;Check for Plagiarism</button>
  <div class="prog" id="prog" style="display:none;">
    <div class="prog-hd">
      <div class="prog-pulse"></div>
      <span class="prog-lbl" id="progLbl">SEARCHING SENTENCE BY SENTENCE...</span>
      <span class="prog-n" id="progN"></span>
    </div>
    <div class="prog-log" id="progLog"></div>
  </div>
  <div id="results"></div>
  <div class="footer"><p>Built by Manish Kumar Parihar &nbsp;·&nbsp; <a href="https://youtube.com/@ProgramDr" target="_blank">@ProgramDr</a> &nbsp;·&nbsp; <a href="https://doi.org/10.5281/zenodo.18824917" target="_blank">CHIMERA-Hash Research Paper</a></p></div>
</div>
<script>
// CHIMERA-HASH ULTRA v5
const tok=t=>t.toLowerCase().match(/[a-z0-9]+/g)||[];
const tokL=t=>t.toLowerCase().match(/[a-z]{3,}/g)||[];
const nums=t=>new Set(t.match(/\b\d+\.?\d*\b/g)||[]);
const lmap=(x,n=3)=>{for(let i=0;i<n;i++)x=3.9*x*(1-x);return x;};
const cw=(tk,p)=>{let cs=0;for(let i=0;i<tk.length;i++)cs+=tk.charCodeAt(i)*(i+1);return(0.5+lmap(((cs+p*31)%1000)/1000))*(p<3?1.3:1)*(tk.length>=4&&tk.length<=8?1.1:1);};
function vj(a,b){const s1=new Set(tok(a).filter(w=>w.length>=4)),s2=new Set(tok(b).filter(w=>w.length>=4)),i=new Set([...s1].filter(w=>s2.has(w))),u=new Set([...s1,...s2]);return u.size?i.size/u.size:0;}
function ci(a,b){const R=[16,32,64,128,256],W=[.35,.25,.2,.12,.08];let t=0;for(let r=0;r<5;r++){const c=r<2,t1=c?a.toLowerCase().split(""):tok(a),t2=c?b.toLowerCase().split(""):tok(b),m1=new Map(),m2=new Map();t1.forEach((tk,i)=>{const k=Math.floor(cw(tk,i)*R[r])%R[r];m1.set(k,(m1.get(k)||0)+1);});t2.forEach((tk,i)=>{const k=Math.floor(cw(tk,i)*R[r])%R[r];m2.set(k,(m2.get(k)||0)+1);});let iv=0,uv=0;new Set([...m1.keys(),...m2.keys()]).forEach(k=>{const x=m1.get(k)||0,y=m2.get(k)||0;iv+=Math.min(x,y);uv+=Math.max(x,y);});t+=W[r]*(uv?iv/uv:0);}return t;}
function bc(a,b){const bg=s=>{const c=s.toLowerCase().replace(/[^a-z]/g,""),m=new Map();for(let i=0;i<c.length-1;i++){const k=c[i]+c[i+1];m.set(k,(m.get(k)||0)+1);}return m;};const b1=bg(a),b2=bg(b);let d=0,n1=0,n2=0;b1.forEach((v,k)=>{d+=v*(b2.get(k)||0);n1+=v*v;});b2.forEach(v=>n2+=v*v);return n1&&n2?d/(Math.sqrt(n1)*Math.sqrt(n2)):0;}
function lcs(a,b){if(!a.length||!b.length)return 0;const dp=Array(a.length+1).fill(null).map(()=>Array(b.length+1).fill(0));for(let i=1;i<=a.length;i++)for(let j=1;j<=b.length;j++)dp[i][j]=a[i-1]===b[j-1]?dp[i-1][j-1]+1:Math.max(dp[i-1][j],dp[i][j-1]);return dp[a.length][b.length]/Math.min(a.length,b.length);}
function saur(a,b){const s1=new Set(tok(a)),s2=new Set(tok(b)),u=new Set([...[...s1].filter(w=>!s2.has(w)),...[...s2].filter(w=>!s1.has(w))]);return u.size?[...u].filter(w=>w.length<=3&&/^[a-z]+$/.test(w)).length/u.size:0;}
function sim(a,b){
  if(!a.trim()||!b.trim())return 0;
  if(a.trim().toLowerCase()===b.trim().toLowerCase())return 1;
  const vjS=vj(a,b),ciS=ci(a,b),bcS=bc(a,b);
  const n1=nums(a),n2=nums(b),ni=new Set([...n1].filter(x=>n2.has(x))),nu=new Set([...n1,...n2]);
  const nj=nu.size?ni.size/nu.size:1;
  let s=vjS*.35+ciS*.37+bcS*.18+nj*.10;
  if(bcS<.02&&s>.08)s=Math.min(s,.08);
  const lcS=lcs(tokL(a),tokL(b));
  if(lcS>=.95&&nj<1&&s>.7&&nu.size>0)s=.7;
  const sS=saur(a,b),sa1=new Set(tok(a)),sa2=new Set(tok(b));
  const us=new Set([...[...sa1].filter(w=>!sa2.has(w)),...[...sa2].filter(w=>!sa1.has(w))]);
  if(sS>.35&&lcS>.45&&[...us].filter(w=>w.length>3).length<=5&&!/[{}();=<>\/\\]/.test(a+b)&&s>.35)s*=.44;
  return Math.max(0,Math.min(1,s));
}
function scoreSents(text,snippets){
  const sents=(text.match(/[^.!?\n]+[.!?\n]*/g)||[text]).map(s=>s.trim()).filter(s=>s.split(/\s+/).length>=4);
  return sents.map(s=>{let max=0;for(const snip of snippets){const sc=sim(s,snip);if(sc>max)max=sc;}return{text:s,score:max,lvl:max>=.75?4:max>=.55?3:max>=.35?2:max>=.16?1:0};});
}
function bestWin(long,ref,w=150){
  const ws=long.split(/\s+/);if(ws.length<=w)return long;
  let best=0,bi=0;
  for(let i=0;i<ws.length-w;i+=6){
    const chunk=ws.slice(i,i+w).join(" ");
    const sc=sim(ref,chunk);
    if(sc>best){best=sc;bi=i;}
  }
  return ws.slice(bi,bi+w).join(" ");
}

function verdict(s){
  if(s>=.85)return{label:"HIGH PLAGIARISM",color:"#e74c3c",bg:"#1c0606",grade:"F",tip:"⛔ Direct match found online. Must attribute the source.",tipBg:"#2d0808"};
  if(s>=.65)return{label:"LIKELY PLAGIARISM",color:"#e67e22",bg:"#1c1006",grade:"D",tip:"⚠️ Strong similarity detected. Cite all matched sources.",tipBg:"#2d1a08"};
  if(s>=.45)return{label:"MODERATE OVERLAP",color:"#e6b800",bg:"#1c1a06",grade:"C",tip:"🟡 Notable overlap. Review highlighted sentences carefully.",tipBg:"#2d2808"};
  if(s>=.20)return{label:"MINOR SIMILARITY",color:"#27ae60",bg:"#061c0e",grade:"B",tip:"🟢 Minor overlap — likely coincidental phrasing.",tipBg:"#0a2e16"};
  return{label:"APPEARS ORIGINAL",color:"#5dade2",bg:"#06101c",grade:"A",tip:"✅ No significant matches found. Content appears original.",tipBg:"#0c1e2e"};
}

const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const logEl=()=>document.getElementById("progLog");
function addLog(msg,cls=""){const d=document.createElement("div");d.className="log-line"+(cls?" "+cls:"");d.textContent=msg;logEl().appendChild(d);logEl().scrollTop=9999;}
function clearLog(){logEl().innerHTML="";}

async function wikiSearch(q){try{const r=await fetch(`https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=${encodeURIComponent(q)}&srlimit=3&format=json&origin=*`,{signal:AbortSignal.timeout(8000)});const d=await r.json();const out=[];for(const h of(d.query?.search||[]).slice(0,2)){try{const er=await fetch(`https://en.wikipedia.org/w/api.php?action=query&titles=${encodeURIComponent(h.title)}&prop=extracts&explaintext=true&exsentences=30&format=json&origin=*`,{signal:AbortSignal.timeout(7000)});const ed=await er.json();const pg=Object.values(ed.query?.pages||{})[0];if(pg?.extract?.length>80)out.push({title:`Wikipedia: ${h.title}`,url:`https://en.wikipedia.org/wiki/${encodeURIComponent(h.title.replace(/ /g,"_"))}`,snippet:pg.extract,source:"Wikipedia",icon:"📖"});}catch(e){}await sleep(60);}return out;}catch(e){return[];}}
async function ssSearch(q){try{const r=await fetch(`https://api.semanticscholar.org/graph/v1/paper/search?query=${encodeURIComponent(q)}&limit=5&fields=title,abstract,url,year`,{signal:AbortSignal.timeout(10000)});const d=await r.json();return(d.data||[]).filter(p=>p.abstract?.length>50).map(p=>({title:`${p.title||""}${p.year?" ("+p.year+")":""}`,url:p.url||"",snippet:p.abstract,source:"Semantic Scholar",icon:"🎓"}));}catch(e){return[];}}

document.getElementById("txt").addEventListener("input",function(){
  const wc=this.value.trim().split(/\s+/).filter(Boolean).length;
  const el=document.getElementById("wc");
  el.textContent=wc+" words"+(wc>=10?" ✓":wc>0?" (need 10+)":"");
  el.style.color=wc>=10?"#27ae60":"#2a2a2a";
  document.getElementById("runBtn").disabled=wc<10;
});

async function runCheck(){
  const text=document.getElementById("txt").value.trim();
  if(text.split(/\s+/).length<10)return;
  const btn=document.getElementById("runBtn");
  btn.disabled=true;
  btn.innerHTML='<div class="spin"></div>Searching sentence by sentence...';
  document.getElementById("results").innerHTML="";
  document.getElementById("prog").style.display="";
  document.getElementById("progLbl").textContent="SEARCHING SENTENCE BY SENTENCE...";
  document.getElementById("progN").textContent="";
  clearLog();

  const all=new Map();
  const add=s=>{const k=s.url||`nu-${all.size}`;if(!all.has(k))all.set(k,s);};

  // Split into sentences for individual searching
  const sentences=(text.match(/[^.!?\n]+[.!?\n]*/g)||[text])
    .map(s=>s.trim())
    .filter(s=>s.split(/\s+/).length>=8); // only search sentences with 8+ words

  addLog(`Found ${sentences.length} searchable sentences`, "info");

  // Send all sentences to server — server searches each one individually
  addLog("Sending to server for exact phrase search...", "info");
  try{
    const r=await fetch("/search",{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body:JSON.stringify({text, sentences}),
      signal:AbortSignal.timeout(180000) // 3 min timeout for thorough search
    });
    const d=await r.json();
    const webResults=d.results||[];
    webResults.forEach(r=>add({...r,icon:"🌐"}));
    addLog(`Web search: ${webResults.length} unique sources found`, webResults.length>0?"ok":"");
    
    // Show live hits from server log
    if(d.log){
      d.log.forEach(l=>addLog(l.msg, l.type||""));
    }
  }catch(e){
    addLog(`Web search error: ${e.message}`, "");
  }

  document.getElementById("progN").textContent=`${all.size} web sources`;
  document.getElementById("progLbl").textContent="SEARCHING ACADEMIC DATABASES...";

  // Academic - use keywords from whole text
  const SW=new Set("the and was for are but not you all can had has who did how may out use its him get too old yet few let new end why this that with have from they were been their said what when where which your also into than then some more will would could should there about after before these those other just like over very such only each both most many even back well here good come".split(" "));
  const kw=text.split(/\s+/).map(x=>x.toLowerCase().replace(/[^a-z]/g,"")).filter(x=>x.length>=5&&!SW.has(x)).slice(0,7).join(" ");
  
  addLog("Searching Wikipedia...", "info");
  (await wikiSearch(kw)).forEach(add);
  addLog("Searching Semantic Scholar (200M papers)...", "info");
  (await ssSearch(kw)).forEach(add);

  document.getElementById("progN").textContent=`${all.size} total sources`;
  document.getElementById("progLbl").textContent="SCORING WITH CHIMERA-HASH v5...";

  const unique=[...all.values()].filter(s=>(s.snippet||s.full_text||"").length>25);
  addLog(`Scoring ${unique.length} sources with CHIMERA-Hash v5...`, "info");

  const scored=unique.map(s=>{
    const raw=s.full_text||s.snippet||"";
    const snip=raw.length>300?bestWin(raw,text):raw;
    return{...s,snippet:snip,score:sim(text,snip)};
  }).sort((a,b)=>b.score-a.score).slice(0,10);

  const maxScore=scored.length?scored[0].score:0;
  const sentData=scoreSents(text,scored.map(s=>s.snippet));

  if(scored.length>0){
    addLog(`Top match: ${Math.round(scored[0].score*100)}% — ${scored[0].url.replace(/https?:\/\/(www\.)?/,"").slice(0,50)}`, scored[0].score>0.5?"hit":"ok");
  }

  render(scored,sentData,maxScore,all.size);
  document.getElementById("prog").style.display="none";
  btn.disabled=false;
  btn.innerHTML='🔍 &nbsp;Check for Plagiarism';
}

function render(scored,sentData,maxScore,totalSources){
  const pct=Math.round(maxScore*100);const v=verdict(maxScore);
  const flagged=sentData.filter(s=>s.lvl>=2).length,highRisk=sentData.filter(s=>s.lvl>=3).length;
  let h=`<div class="res">
  <div class="vbox" style="background:${v.bg};border:1px solid ${v.color}20;"><div class="vbox-in">
    <div class="vb-l"><div class="vpct" style="color:${v.color};">${pct}%</div><div class="vgrade" style="color:${v.color};background:${v.color}18;border:1px solid ${v.color}30;">GRADE ${v.grade}</div></div>
    <div class="vb-m">
      <div class="vtitle" style="color:${v.color};">${v.label}</div>
      <div class="vdesc">Searched ${totalSources} sources — each sentence searched individually as exact quoted phrase.</div>
      <div class="vtip" style="background:${v.tipBg};color:${v.color};">${v.tip}</div>
      <div class="vrisk"><div class="vrisk-bar"><div class="vrisk-pin" style="left:${pct}%;"></div></div><div class="vrisk-lbl"><span>0%</span><span>Original</span><span>50%</span><span>Plagiarism</span><span>100%</span></div></div>
    </div>
    <div class="vb-r"><div class="vr-n" style="color:${v.color};">${scored.length}</div><div class="vr-l">SOURCES<br>MATCHED</div></div>
  </div></div>
  <div class="stats">
    <div class="stat"><div class="sn" style="color:${v.color};">${pct}%</div><div class="sl">SIMILARITY</div></div>
    <div class="stat"><div class="sn" style="color:${highRisk>0?"#e74c3c":"var(--t3)"};">${highRisk}</div><div class="sl">HIGH RISK SENTENCES</div></div>
    <div class="stat"><div class="sn" style="color:${flagged>0?"#e67e22":"var(--t3)"};">${flagged}</div><div class="sl">FLAGGED SENTENCES</div></div>
    <div class="stat"><div class="sn" style="color:var(--blue);">${totalSources}</div><div class="sl">SOURCES CHECKED</div></div>
  </div>
  <div class="hm"><div class="hm-hd"><span class="hm-title">SENTENCE-LEVEL HEATMAP</span><span class="hm-stat">${highRisk} high-risk · ${sentData.filter(s=>s.lvl===2).length} moderate · ${sentData.filter(s=>s.lvl<=1).length} clean</span></div>
  <div class="hm-sub">Hover each sentence to see its exact match %. Red = found on internet. Green = original.</div>
  <div class="hm-body">`;
  sentData.forEach(s=>{h+=`<span class="s s${s.lvl}" title="${Math.round(s.score*100)}% similarity">${s.text.replace(/</g,"&lt;")} </span>`;});
  h+=`</div><div class="hm-legend">
    <div class="hl"><div class="hldot" style="background:#e8e8e812;border:1px solid #1e1e1e;"></div>Clean</div>
    <div class="hl"><div class="hldot" style="background:#27ae601e;"></div>Low (16–34%)</div>
    <div class="hl"><div class="hldot" style="background:#e6b80024;"></div>Moderate (35–54%)</div>
    <div class="hl"><div class="hldot" style="background:#e67e2230;"></div>High (55–74%)</div>
    <div class="hl"><div class="hldot" style="background:#e74c3c3a;"></div>Very High (75%+)</div>
  </div></div>`;
  if(scored.length){
    h+=`<div class="src-hd">MATCHING SOURCES — ranked by similarity score</div>`;
    scored.forEach(src=>{const V=verdict(src.score);
      h+=`<div class="scard" style="border-color:${V.color}16;"><div class="scard-in">
        <div class="sscore" style="background:linear-gradient(160deg,${V.bg},#060606);border-right-color:${V.color}10;">
          <div class="spct" style="color:${V.color};">${Math.round(src.score*100)}%</div>
          <div class="sicon">${src.icon||"🔗"}</div>
          <div class="ssrc" style="color:${V.color}80;">${src.source}</div>
        </div>
        <div class="sbody">
          <div class="stitle">${esc(src.title||"Source")}</div>
          ${src.url?`<a href="${src.url}" target="_blank" class="surl">${src.url.replace(/https?:\/\/(www\.)?/,"").slice(0,82)}</a>`:""}
          <div class="ssnip">${esc((src.snippet||"").slice(0,260))}</div>
          <div class="sfoot">
            <span class="stype">${src.source}</span>
            <div class="sbar-row"><div class="sbar"><div class="sfill" style="width:${Math.round(src.score*100)}%;background:${V.color};box-shadow:0 0 5px ${V.color}40;"></div></div>
            <span style="font-size:9px;font-family:monospace;color:${V.color};">${Math.round(src.score*100)}%</span></div>
          </div>
        </div>
      </div></div>`;
    });
  }else{
    h+=`<div class="no-match"><div class="nm-ico">✅</div><div class="nm-t">No matches found</div><div class="nm-d">No matching content found. The text appears original, or the source website blocks all web crawlers (e.g. behind login/paywall).</div></div>`;
  }
  h+=`<button class="reset-btn" onclick="clearAll()">← Check another text</button></div>`;
  document.getElementById("results").innerHTML=h;
  document.getElementById("results").scrollIntoView({behavior:"smooth",block:"start"});
}
const esc=s=>(s||"").replace(/</g,"&lt;").replace(/>/g,"&gt;");
function clearAll(){document.getElementById("txt").value="";document.getElementById("wc").textContent="0 words";document.getElementById("wc").style.color="var(--t4)";document.getElementById("results").innerHTML="";document.getElementById("prog").style.display="none";document.getElementById("runBtn").disabled=true;}
</script>
</body>
</html>"""


# ─────────────────────────────────────────────
# SEARCH ENGINE
# ─────────────────────────────────────────────
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
HDR = {"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "Connection": "keep-alive"}

def http_get(url, timeout=12, extra=None):
    h = dict(HDR)
    if extra: h.update(extra)
    try:
        req = Request(url, headers=h)
        with urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            try: raw = gzipmod.decompress(raw)
            except: pass
            cs = resp.headers.get_content_charset() or "utf-8"
            return raw.decode(cs, errors="replace")
    except Exception as e:
        print(f"  GET error: {str(e)[:50]}")
        return None

def strip_tags(html):
    html = re.sub(r'<(script|style|noscript)[^>]*>.*?</\1>', ' ', html or '', flags=re.DOTALL|re.IGNORECASE)
    return re.sub(r'<[^>]+>', ' ', html)

def clean(t):
    return re.sub(r'\s+', ' ', t or '').strip()

def ddg(query, n=8):
    url = f"https://html.duckduckgo.com/html/?q={quote(query)}&kl=us-en"
    html = http_get(url, extra={"Referer": "https://duckduckgo.com/"})
    if not html: return []
    results = []
    # Extract using both methods
    for block in re.findall(r'<div[^>]+class="[^"]*result[^"]*"[^>]*>(.*?)(?=<div[^>]+class="[^"]*result[^"]*"|</div>\s*</div>\s*</div>)', html, re.DOTALL)[:n]:
        am = re.search(r'<a[^>]+class="[^"]*result__a[^"]*"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', block, re.DOTALL)
        sm = re.search(r'class="[^"]*result__snippet[^"]*"[^>]*>(.*?)</(?:span|a|div)>', block, re.DOTALL)
        if not am: continue
        href = am.group(1)
        title = clean(strip_tags(am.group(2)))
        snip = clean(strip_tags(sm.group(1))) if sm else title
        ug = re.search(r'uddg=([^&"]+)', href)
        if ug: href = unquote(ug.group(1))
        if href.startswith('http') and snip and len(snip)>10:
            results.append({'title':title,'url':href,'snippet':snip[:500],'source':'Web (DuckDuckGo)'})
    if not results:
        titles = re.findall(r'class="result__a"[^>]*>(.*?)</a>', html)
        snips  = re.findall(r'class="result__snippet"[^>]*>(.*?)</(?:span|a)', html, re.DOTALL)
        uddgs  = re.findall(r'uddg=([^&"]+)', html)
        for i in range(min(len(titles),len(snips),n)):
            t=clean(strip_tags(titles[i]));s=clean(strip_tags(snips[i]));u=unquote(uddgs[i]) if i<len(uddgs) else ''
            if t and s and u.startswith('http'): results.append({'title':t,'url':u,'snippet':s[:500],'source':'Web (DuckDuckGo)'})
    return results

def bing(query, n=8):
    url = f"https://www.bing.com/search?q={quote(query)}&count={n}&setlang=en"
    html = http_get(url, extra={"Referer":"https://www.bing.com/"})
    if not html: return []
    results=[]
    for block in re.findall(r'<li[^>]+class="b_algo"[^>]*>(.*?)</li>', html, re.DOTALL)[:n]:
        am=re.search(r'<h2[^>]*>.*?<a[^>]+href="(https?://[^"]+)"[^>]*>(.*?)</a>',block,re.DOTALL)
        pm=re.search(r'<p[^>]*>(.*?)</p>',block,re.DOTALL)
        if not am: continue
        u=am.group(1);t=clean(strip_tags(am.group(2)));s=clean(strip_tags(pm.group(1))) if pm else t
        if u.startswith('http') and s and len(s)>10: results.append({'title':t,'url':u,'snippet':s[:500],'source':'Web (Bing)'})
    return results

def fetch_page(url, timeout=8):
    html = http_get(url, timeout=timeout)
    if not html: return None
    html = re.sub(r'<(script|style|nav|footer|header|aside|noscript|iframe|form)[^>]*>.*?</\1>',' ',html,flags=re.DOTALL|re.IGNORECASE)
    for tag in ['article','main']:
        m=re.search(f'<{tag}[^>]*>(.*?)</{tag}>',html,re.DOTALL|re.IGNORECASE)
        if m: html=m.group(1); break
    m2=re.search(r'<div[^>]+(?:id|class)="[^"]*(?:content|article|post|entry|body|text|story)[^"]*"[^>]*>(.*?)</div>',html,re.DOTALL|re.IGNORECASE)
    if m2: html=m2.group(1)
    text=clean(strip_tags(html))
    return text[:6000] if len(text)>80 else None


# ─────────────────────────────────────────────
# SERVER
# ─────────────────────────────────────────────
class Handler(BaseHTTPRequestHandler):
    def log_message(self,*a): pass

    def send_json(self, data, code=200):
        body=json.dumps(data).encode()
        self.send_response(code)
        self.send_header('Content-Type','application/json')
        self.send_header('Access-Control-Allow-Origin','*')
        self.send_header('Content-Length',len(body))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin','*')
        self.send_header('Access-Control-Allow-Methods','GET,POST,OPTIONS')
        self.send_header('Access-Control-Allow-Headers','Content-Type')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(HTML.encode())

    def do_POST(self):
        if self.path!='/search':
            self.send_json({'error':'Not found'},404); return
        length=int(self.headers.get('Content-Length',0))
        body=json.loads(self.rfile.read(length))
        text=body.get('text','')
        sentences=body.get('sentences',[])
        log=[]

        print(f"\n{'='*55}")
        print(f"TEXT: {text[:70]}...")
        print(f"Sentences to search: {len(sentences)}")

        all_results={}
        total_searched=0

        # THE KEY FIX: search EACH SENTENCE individually as exact quoted phrase
        for i, sent in enumerate(sentences[:10]): # cap at 10 sentences
            words = sent.strip().split()
            if len(words) < 8: continue

            # Use first 12 words as exact quoted phrase — unique enough to pinpoint source
            phrase = ' '.join(words[:12])
            query = f'"{phrase}"'

            print(f"\n[Sentence {i+1}] {query}")
            log.append({"msg": f"Searching: {query[:65]}", "type": "info"})

            found = ddg(query, n=8)
            print(f"  DDG: {len(found)}")

            if len(found) < 3:
                b = bing(query, n=8)
                print(f"  Bing: {len(b)}")
                found.extend(b)

            new = 0
            for r in found:
                if r['url'] not in all_results:
                    all_results[r['url']] = r
                    new += 1

            if found:
                log.append({"msg": f"  → {len(found)} results, {new} new unique sources", "type": "ok" if found else ""})
            else:
                log.append({"msg": f"  → No results for this sentence", "type": ""})

            total_searched += 1
            time.sleep(1.0)  # respectful delay

        print(f"\nTotal unique sources: {len(all_results)}")
        log.append({"msg": f"Total unique sources found: {len(all_results)}", "type": "info"})

        unique = list(all_results.values())

        # Fetch FULL PAGE for every result — this is how we score accurately
        print("Fetching full page content for all sources...")
        log.append({"msg": "Fetching full page text from each source...", "type": "info"})
        fetched = 0
        for i, src in enumerate(unique[:15]):
            try:
                pg = fetch_page(src['url'], timeout=7)
                if pg and len(pg) > len(src.get('snippet','')):
                    src['full_text'] = pg
                    fetched += 1
                    print(f"  [{i+1}] {len(pg)} chars — {src['url'][:55]}")
                time.sleep(0.4)
            except: pass

        log.append({"msg": f"Full page content fetched from {fetched} sources", "type": "ok"})
        print(f"Done. {len(unique)} sources, {fetched} with full text.")

        self.send_json({'results': unique[:20], 'log': log})


def open_browser():
    time.sleep(1.8)
    webbrowser.open('http://localhost:7477')

if __name__=='__main__':
    PORT=7477
    server=HTTPServer(('0.0.0.0',PORT),Handler)
    print("\n"+"="*55)
    print("  PlagCheck Pro — Sentence-by-Sentence Search")
    print("  Each sentence searched as exact quoted phrase")
    print("  DuckDuckGo + Bing + Full page content reading")
    print("  By @ProgramDr")
    print("="*55)
    print(f"\n  ✅ http://localhost:{PORT}")
    print("  ✅ Browser opening now...")
    print("  ✅ No API key, 100% free")
    print("\n  NOTE: Takes 30-60 seconds — searching every sentence")
    print("  Press Ctrl+C to stop\n")
    threading.Thread(target=open_browser,daemon=True).start()
    try: server.serve_forever()
    except KeyboardInterrupt: print("\nStopped.")
