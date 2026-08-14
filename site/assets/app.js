const search = document.querySelector('#search');
const filters = [...document.querySelectorAll('[data-filter]')];
const cards = [...document.querySelectorAll('.day-card')];
const empty = document.querySelector('.empty');

function applyFilters() {
  const q = (search?.value || '').toLowerCase().trim();
  const active = document.querySelector('[data-filter].active')?.dataset.filter || 'all';
  let visible = 0;

  cards.forEach((card) => {
    const phaseOk = active === 'all' || card.dataset.phase === active;
    const textOk = !q || card.textContent.toLowerCase().includes(q);
    const show = phaseOk && textOk;
    card.style.display = show ? '' : 'none';
    if (show) visible += 1;
  });

  if (empty) empty.style.display = visible ? 'none' : 'block';
}

filters.forEach((btn) =>
  btn.addEventListener('click', () => {
    filters.forEach((b) => b.classList.remove('active'));
    btn.classList.add('active');
    applyFilters();
  }),
);

search?.addEventListener('input', applyFilters);

document.querySelectorAll('.checklist input').forEach((box, idx) => {
  const key = `${location.pathname}:check:${idx}`;
  box.checked = localStorage.getItem(key) === '1';
  box.addEventListener('change', () => localStorage.setItem(key, box.checked ? '1' : '0'));
});
