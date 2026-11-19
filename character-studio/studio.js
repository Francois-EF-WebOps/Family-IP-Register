(() => {
  "use strict";
  const $ = (id) => document.getElementById(id);
  const STORAGE_KEY = "family-ip-character-studio-v1";
  let fixtures = {};
  let current = null;
  let originalIdentity = null;

  const escapeXml = (value) => String(value ?? "").replace(/[&<>"']/g, (c) => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&apos;"}[c]));
  const clone = (value) => JSON.parse(JSON.stringify(value));

  function setMessage(message) { $("message").textContent = message; }
  function activeCharacter() { return current; }

  function renderSvg(character) {
    const id = character.character_id;
    const skin = id === "character.fin" ? "#75452f" : "#c58b63";
    const hair = id === "character.fin" ? "#201b1a" : "#35251f";
    const garment = character.appearance.garment_colour;
    const hairShape = id === "character.fin"
      ? '<path d="M128 111 Q122 63 170 62 Q218 64 212 111 L203 99 Q194 85 182 92 Q168 78 154 94 Q140 87 135 108Z" fill="'+hair+'"/>'
      : '<path d="M122 119 Q112 55 169 55 Q225 57 217 124 L218 204 Q201 222 190 197 L193 112 Q169 94 145 112 L145 203 Q127 218 119 196Z" fill="'+hair+'"/><path d="M132 83 Q165 47 203 77 Q211 89 202 99 Q169 80 139 103Z" fill="'+hair+'"/>';
    const accessory = character.appearance.show_accessory
      ? (id === "character.fin"
        ? '<path d="M229 220 L272 300" stroke="#8c6338" stroke-width="5" stroke-linecap="round"/><path d="M267 293 l12 16" stroke="#8c6338" stroke-width="3"/>'
        : '<path d="M222 235 Q260 224 269 265 L258 300 L222 291Z" fill="#b88c55" stroke="#765b38" stroke-width="3"/><path d="M224 240 Q244 225 263 242" fill="none" stroke="#765b38" stroke-width="3"/><circle cx="238" cy="258" r="7" fill="#c96b45"/><circle cx="253" cy="267" r="7" fill="#d6a54d"/><path d="M241 247 q-8 -12 -14 -6" fill="none" stroke="#54704b" stroke-width="3"/>')
      : "";
    let garmentShape = "";
    if (character.appearance.garment_style === "cape") {
      garmentShape = '<path d="M137 167 L202 167 L230 280 L108 280Z" fill="'+garment+'" stroke="#665c4f" stroke-width="2"/>';
    } else if (character.appearance.garment_style === "shirt") {
      garmentShape = '<path d="M140 165 L112 184 L125 214 L140 203 L140 283 L200 283 L200 203 L215 214 L229 184 L201 165 L184 176 L158 176Z" fill="'+garment+'" stroke="#665c4f" stroke-width="2"/>';
    } else {
      garmentShape = '<path d="M139 164 L157 174 L184 174 L202 164 L220 189 L202 210 L198 286 L141 286 L137 210 L119 189Z" fill="'+garment+'" stroke="#665c4f" stroke-width="2"/>';
    }
    const lower = id === "character.fin"
      ? '<path d="M144 282 L169 282 L166 341 L139 341Z M174 282 L198 282 L204 341 L177 341Z" fill="#d7c7a5" stroke="#665c4f" stroke-width="2"/>'
      : '<path d="M143 282 L169 282 L166 341 L139 341Z M174 282 L199 282 L204 341 L177 341Z" fill="#d7c7a5" stroke="#665c4f" stroke-width="2"/>';
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 390" role="img" aria-label="Stylised '+escapeXml(character.name)+' character illustration"><rect width="340" height="390" rx="18" fill="#f7f3e9"/><ellipse cx="170" cy="356" rx="66" ry="9" fill="#ded7c9"/><path d="M151 128 Q170 113 189 128 L191 164 L149 164Z" fill="'+skin+'"/><path d="M126 105 Q127 70 169 68 Q212 69 214 108 Q211 149 170 157 Q129 148 126 105Z" fill="'+skin+'" stroke="#573c30" stroke-width="2"/>'+hairShape+'<ellipse cx="151" cy="117" rx="5" ry="7" fill="#2a211d"/><ellipse cx="189" cy="117" rx="5" ry="7" fill="#2a211d"/><path d="M162 133 Q170 138 178 132" fill="none" stroke="#6f3f32" stroke-width="2" stroke-linecap="round"/><g fill="#5b3429"><circle cx="143" cy="130" r="1.8"/><circle cx="150" cy="135" r="1.5"/><circle cx="195" cy="132" r="1.8"/><circle cx="188" cy="137" r="1.5"/></g>'+garmentShape+lower+'<path d="M143 340 L165 340 L165 350 L133 350 Q132 344 143 340 M179 340 L202 340 L210 350 L178 350Z" fill="'+skin+'"/>'+accessory+'<text x="170" y="378" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#65777a">'+escapeXml(character.name.toUpperCase())+' · DRAFT STUDY</text></svg>';
  }

  function updatePreview() {
    if (!current) return;
    $("preview-name").textContent = current.name;
    $("preview").innerHTML = renderSvg(current);
    $("identity-summary").textContent = current.identity.age_years + " years · " + current.identity.gender_presentation + " · " + current.identity.skin_description + " · " + current.identity.hair_description + " · " + current.identity.eye_description + ".";
  }

  function selectCharacter(key) {
    current = clone(fixtures[key]);
    originalIdentity = JSON.stringify(current.identity);
    $("garment-colour").value = current.appearance.garment_colour;
    $("garment-style").value = current.appearance.garment_style;
    $("show-accessory").checked = current.appearance.show_accessory;
    updatePreview();
    setMessage("Loaded documented fixture: " + current.name + ".");
  }

  function applyAppearance() {
    if (!current) return;
    current.appearance.garment_colour = $("garment-colour").value;
    current.appearance.garment_style = $("garment-style").value;
    current.appearance.show_accessory = $("show-accessory").checked;
    if (JSON.stringify(current.identity) !== originalIdentity) {
      current.identity = JSON.parse(originalIdentity);
      setMessage("Identity is locked. Appearance updated; identity changes were discarded.");
    } else setMessage("Appearance updated. Identity remains unchanged.");
    updatePreview();
  }

  function download(filename, content, type) {
    const blob = new Blob([content], {type});
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url; a.download = filename; a.click();
    URL.revokeObjectURL(url);
  }

  async function init() {
    try {
      const response = await fetch("./characters.json");
      if (!response.ok) throw new Error("Could not load character fixtures.");
      const data = await response.json();
      fixtures = data.characters;
      selectCharacter("fin");
    } catch (error) {
      setMessage(error.message + " Open this page through GitHub Pages or a local web server.");
    }
  }

  $("character-select").addEventListener("change", (event) => selectCharacter(event.target.value));
  ["garment-colour","garment-style","show-accessory"].forEach((id) => $(id).addEventListener("change", applyAppearance));
  $("save-local").addEventListener("click", () => {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(current));
    setMessage("Saved on this device in this browser only.");
  });
  $("load-local").addEventListener("click", () => {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return setMessage("No local save found on this device.");
    try {
      const saved = JSON.parse(raw);
      const fixture = fixtures[$("character-select").value];
      if (!fixture || saved.character_id !== fixture.character_id) throw new Error("Saved character does not match the selected fixture.");
      current = clone(fixture);
      current.appearance = {...current.appearance, ...saved.appearance};
      originalIdentity = JSON.stringify(current.identity);
      $("garment-colour").value = current.appearance.garment_colour;
      $("garment-style").value = current.appearance.garment_style;
      $("show-accessory").checked = current.appearance.show_accessory;
      updatePreview();
      setMessage("Saved appearance loaded. Canonical identity restored from fixture.");
    } catch (error) { setMessage("Could not load save: " + error.message); }
  });
  $("reset").addEventListener("click", () => selectCharacter($("character-select").value));
  $("download-json").addEventListener("click", () => {
    const exported = clone(current);
    exported.provenance.exported_at = new Date().toISOString();
    exported.provenance.review_status = "DRAFT_REQUIRES_HUMAN_REVIEW";
    download(current.character_id.replaceAll(".","-")+".json", JSON.stringify(exported,null,2)+"\n", "application/json");
  });
  $("download-svg").addEventListener("click", () => download(current.character_id.replaceAll(".","-")+".svg", renderSvg(current), "image/svg+xml"));
  init();
})();