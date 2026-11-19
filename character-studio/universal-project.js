/* Universal project envelope: renderer- and provider-neutral. */
(() => {
  "use strict";
  const TYPES = ["prompt", "script", "image", "json", "gltf", "glb", "text", "unknown"];
  const makeId = () => (globalThis.crypto && crypto.randomUUID) ? crypto.randomUUID() : "src-" + Date.now().toString(36) + "-" + Math.random().toString(36).slice(2, 9);
  function create(title) {
    const now = new Date().toISOString();
    return {project_schema_version:1, project_id:"project-" + makeId(), title:String(title || "Untitled creative project").trim(), created_at:now, updated_at:now, sources:[], decisions:[], exports:[], status:"working_draft"};
  }
  function addSource(project, input) {
    if (!project || project.project_schema_version !== 1 || !Array.isArray(project.sources)) throw new Error("Unsupported project envelope.");
    const type = TYPES.includes(input.type) ? input.type : "unknown";
    const source = {source_id:makeId(), type, name:String(input.name || type + " source").slice(0,240), mime_type:String(input.mime_type || "text/plain").slice(0,120), size_bytes:Number.isFinite(input.size_bytes) ? Math.max(0,input.size_bytes) : 0, role:String(input.role || "unassigned"), status:String(input.status || "received"), added_at:new Date().toISOString(), ...(typeof input.content === "string" ? {content:input.content} : {}), ...(input.metadata && typeof input.metadata === "object" ? {metadata:input.metadata} : {})};
    project.sources.push(source); project.updated_at=new Date().toISOString(); return source;
  }
  function validate(project) {
    return Boolean(project && project.project_schema_version === 1 && typeof project.project_id === "string" && typeof project.title === "string" && Array.isArray(project.sources) && project.sources.every((source) => source && typeof source.source_id === "string" && TYPES.includes(source.type) && typeof source.name === "string" && typeof source.role === "string"));
  }
  function exportManifest(project) { if (!validate(project)) throw new Error("Project failed validation."); return JSON.stringify(project,null,2) + "\n"; }
  window.UniversalProject = Object.freeze({create,addSource,validate,exportManifest,types:TYPES});
})();