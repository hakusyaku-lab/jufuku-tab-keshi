const api = globalThis.browser ?? globalThis.chrome;

function key(url) {
  try {
    const u = new URL(url);
    u.hash = "";
    let s = u.toString();
    if (s.endsWith("/")) s = s.slice(0, -1);
    return s;
  } catch { return url; }
}

api.action.onClicked.addListener(async () => {
  const tabs = await api.tabs.query({});
  // 残す優先順位: 固定タブ > 表示中のタブ > 左にあるタブ
  tabs.sort((a, b) =>
    (b.pinned - a.pinned) || (b.active - a.active) ||
    (a.windowId - b.windowId) || (a.index - b.index));
  const seen = new Set();
  const close = [];
  for (const t of tabs) {
    const url = t.url || t.pendingUrl;
    if (!url) continue;
    const k = key(url);
    if (seen.has(k)) close.push(t.id); else seen.add(k);
  }
  if (close.length) await api.tabs.remove(close);
  await api.action.setBadgeText({ text: String(close.length) });
  setTimeout(() => api.action.setBadgeText({ text: "" }), 4000);
});
