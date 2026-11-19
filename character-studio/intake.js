/* Open-entry intake UI. Files remain in this browser session; no upload occurs. */
(() => {
  "use strict";
  const $ = (id) => document.getElementById(id);
  const project = window.UniversalProject.create("Untitled creative project");
  const downloads = new Map();
  const classify = (file) => {
    const name=file.name.toLowerCase();
    if(file.type.startsWith("image/")) return "image";
    if(name.endsWith(".glb")) return "glb";
    if(name.endsWith(".gltf")) return "gltf";
    if(name.endsWith(".json")) return "json";
    if(name.endsWith(".md") || name.endsWith(".txt")) return "script";
    return "unknown";
  };
  function setStatus(message){ $("intake-status").textContent=message; }
  function addCard(source,previewUrl){
    const card=document.createElement("article"); card.className="source-card";
    const heading=document.createElement("strong"); heading.textContent=source.name;
    const meta=document.createElement("p"); meta.className="muted small"; meta.textContent=source.type.toUpperCase()+" · "+source.size_bytes.toLocaleString()+" bytes · "+source.status;
    const role=document.createElement("label"); role.textContent="Source role";
    const select=document.createElement("select"); select.setAttribute("aria-label","Role for "+source.name);
    [["unassigned","Unassigned"],["identity","Identity / person"],["body","Body / proportions"],["style","Art direction / style"],["wardrobe","Clothing / appearance"],["environment","Environment / setting"],["story","Script / narrative"],["geometry","3D geometry"],["other","Other"]].forEach(([value,label])=>{const option=document.createElement("option");option.value=value;option.textContent=label;select.append(option);});
    select.value=source.role; select.addEventListener("change",()=>{source.role=select.value;project.updated_at=new Date().toISOString();}); role.append(select); card.append(heading,meta,role);
    if(previewUrl && source.type==="image"){const img=document.createElement("img");img.src=previewUrl;img.alt="Preview of "+source.name;img.className="source-thumbnail";card.append(img);}
    else if(["prompt","script","text","json"].includes(source.type)){const pre=document.createElement("pre");pre.className="source-text";pre.textContent=(source.content||"").slice(0,900);card.append(pre);}
    else if(source.type==="glb" || source.type==="gltf"){const note=document.createElement("p");note.className="muted small";note.textContent=source.type==="glb"?"GLB asset recognised and retained. Interactive 3D rendering is not part of this intake increment.":"glTF manifest recognised. External buffers and textures may need to be supplied alongside it.";card.append(note);}
    else {const note=document.createElement("p");note.className="muted small";note.textContent="Unclassified source received. Original file is available below.";card.append(note);}
    const link=document.createElement("a");link.href=downloads.get(source.source_id)||"#";link.textContent="Download original";link.className="source-download";if(downloads.has(source.source_id))link.download=source.name;card.append(link);
    $("source-list").prepend(card);
  }
  async function addFile(file){
    const type=classify(file); let content; let status="received"; let metadata={};
    if(["json","gltf","script"].includes(type)){content=await file.text();if(type==="json"||type==="gltf"){try{const parsed=JSON.parse(content);metadata={top_level_type:Array.isArray(parsed)?"array":typeof parsed,top_level_keys:parsed&&!Array.isArray(parsed)&&typeof parsed==="object"?Object.keys(parsed).slice(0,40):[]};status="parsed";}catch(_){status="invalid_json";}}}
    else if(type==="image")metadata={preview_available:true};
    else if(type==="glb")metadata={container:"glb",renderer_status:"pending_integration"};
    const source=window.UniversalProject.addSource(project,{type,name:file.name,mime_type:file.type||"application/octet-stream",size_bytes:file.size,status,...(content!==undefined?{content}:{}),metadata});
    const url=URL.createObjectURL(file);downloads.set(source.source_id,url);addCard(source,type==="image"?url:null);
    setStatus(file.name+(status==="invalid_json"?" received, but JSON parsing failed.":" added to this workspace."));
  }
  function addText(type,value){
    const content=value.trim();if(!content)return setStatus("Enter a prompt or script first.");
    const source=window.UniversalProject.addSource(project,{type,name:type==="prompt"?"User prompt":"User script",mime_type:"text/plain",size_bytes:new Blob([content]).size,role:type==="script"?"story":"unassigned",content,status:"received"});
    addCard(source,null);$("prompt-input").value="";setStatus(type==="prompt"?"Prompt added as source material. No AI generation is implied.":"Script added to this workspace.");
  }
  function updateManifest(){project.title=$("project-title").value.trim()||"Untitled creative project";$("source-count").textContent=project.sources.length+" source"+(project.sources.length===1?"":"s");$("export-project").disabled=!project.sources.length;}
  $("add-prompt").addEventListener("click",()=>{addText("prompt",$("prompt-input").value);updateManifest();});
  $("add-script").addEventListener("click",()=>{addText("script",$("prompt-input").value);updateManifest();});
  $("source-files").addEventListener("change",async(event)=>{for(const file of Array.from(event.target.files||[]))await addFile(file);event.target.value="";updateManifest();});
  $("project-title").addEventListener("input",updateManifest);
  $("export-project").addEventListener("click",()=>{updateManifest();const blob=new Blob([window.UniversalProject.exportManifest(project)],{type:"application/json"});const url=URL.createObjectURL(blob);const a=document.createElement("a");a.href=url;a.download="creative-project-manifest.json";a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);setStatus("Manifest exported. Download original files individually to retain binary contents; the manifest records their metadata and text.");});
  window.addEventListener("beforeunload",()=>{for(const url of downloads.values())URL.revokeObjectURL(url);});
  updateManifest();
})();