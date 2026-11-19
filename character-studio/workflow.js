/* Reusable workflow-state helpers. No network, framework, or account dependency. */
(() => {
  "use strict";
  const STATUS = ["not_started", "in_progress", "blocked", "complete"];
  const MISSING_STATES = ["unknown", "incomplete", "conflict", "verified"];
  function create(projectId, stageDefinitions) {
    const stages = stageDefinitions.map((stage) => ({
      stage_id: stage.id,
      label: stage.label,
      status: "not_started",
      missing: []
    }));
    if (stages.length) stages[0].status = "in_progress";
    return {
      workflow_version: 1,
      project_id: projectId,
      current_stage: stages[0]?.stage_id || "",
      stages,
      updated_at: new Date().toISOString()
    };
  }
  function validate(state) {
    if (!state || state.workflow_version !== 1 || typeof state.project_id !== "string" ||
        !Array.isArray(state.stages) || !state.stages.length ||
        !state.stages.some((stage) => stage.stage_id === state.current_stage)) return false;
    return state.stages.every((stage) =>
      typeof stage.stage_id === "string" &&
      STATUS.includes(stage.status) &&
      Array.isArray(stage.missing) &&
      stage.missing.every((item) => typeof item.field === "string" && MISSING_STATES.includes(item.state))
    );
  }
  function setCurrentStage(state, stageId) {
    if (!state.stages.some((stage) => stage.stage_id === stageId)) throw new Error("Unknown workflow stage.");
    state.current_stage = stageId;
    const stage = state.stages.find((item) => item.stage_id === stageId);
    if (stage.status === "not_started") stage.status = "in_progress";
    state.updated_at = new Date().toISOString();
    return state;
  }
  function updateMissing(state, stageId, entries) {
    const stage = state.stages.find((item) => item.stage_id === stageId);
    if (!stage) throw new Error("Unknown workflow stage.");
    stage.missing = entries.filter((item) => item.field.trim()).map((item) => ({
      field: item.field.trim(),
      state: MISSING_STATES.includes(item.state) ? item.state : "unknown",
      ...(item.note ? {note: item.note} : {})
    }));
    state.updated_at = new Date().toISOString();
    return state;
  }
  window.CharacterWorkflow = Object.freeze({create, validate, setCurrentStage, updateMissing, statuses: STATUS, missingStates: MISSING_STATES});
})();
