import re

def rewrite():
    files = ["c:\\Users\\Anonimo\\Documents\\Work\\CAS\\cas.html", "c:\\Users\\Anonimo\\Documents\\Work\\CAS\\index.html"]
    
    html_content = None
    target_file = None
    for f in files:
        try:
            with open(f, "r", encoding="utf-8") as file:
                html_content = file.read()
                target_file = f
                break
        except FileNotFoundError:
            continue
            
    if not html_content:
        print("Could not find HTML file.")
        return

    new_css = """
/* ── TOKENS ─────────────────────────────────────────────── */
:root{
  --bg:        #f8fafc;
  --bg1:       #ffffff;
  --bg2:       #f1f5f9;
  --surface:   rgba(255, 255, 255, 0.65);
  --ink:       #0f172a;
  --ink2:      #334155;
  --muted:     #64748b;
  --border:    rgba(15, 23, 42, 0.08);
  --border2:   rgba(47, 92, 95, 0.15);
  
  --teal:      #2f5c5f;
  --teal-mid:  #3d767a;
  --teal-lt:   #529da1;
  --teal-pale: #ebf2f2;
  --teal-pale2:#d5e5e6;
  --accent:    #2f5c5f;
  
  --r:         12px;
  --r2:        24px;
  --font-head: 'Plus Jakarta Sans', 'Inter', sans-serif;
  --font-body: 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --ease:      cubic-bezier(.16,1,.3,1);
  --shadow:    0 8px 32px rgba(15, 23, 42, 0.04);
  --shadow2:   0 16px 48px rgba(15, 23, 42, 0.08);
}

/* ── RESET ──────────────────────────────────────────────── */
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-font-smoothing:antialiased}
body{background:var(--bg);color:var(--ink);font-family:var(--font-body);font-size:16px;line-height:1.65;overflow-x:hidden}
a{color:inherit;text-decoration:none}
ul{list-style:none}
button{cursor:pointer;border:none;background:none;font-family:inherit}
input,textarea,select{font-family:inherit}
::-webkit-scrollbar{width:4px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--teal-lt);border-radius:10px}

/* ── TYPOGRAPHY ─────────────────────────────────────────── */
.label{font-family:var(--font-mono);font-size:.7rem;letter-spacing:.15em;text-transform:uppercase;color:var(--teal)}
h1,h2,h3,h4{font-family:var(--font-head);line-height:1.15;color:var(--ink)}
h1{font-size:clamp(3rem,6.5vw,5.5rem);letter-spacing:-.03em;font-weight:800}
h2{font-size:clamp(2.2rem,4vw,3.5rem);letter-spacing:-.02em;font-weight:800}
h3{font-size:1.35rem;font-weight:700;letter-spacing:-.01em}
p{color:var(--muted);line-height:1.8;font-size:1rem}
em.styled{font-style:normal;color:var(--teal);position:relative;display:inline-block}

/* ── LAYOUT ─────────────────────────────────────────────── */
.container{max-width:1200px;margin:0 auto;padding:0 32px}
section{position:relative}

/* ── DIVIDER ────────────────────────────────────────────── */
.rule{width:40px;height:3px;background:var(--teal);margin-bottom:24px;display:block;border-radius:2px}

/* ── BUTTONS ────────────────────────────────────────────── */
.btn{
  display:inline-flex;align-items:center;gap:10px;
  padding:14px 28px;border-radius:var(--r);
  font-family:var(--font-head);font-size:.9rem;font-weight:600;
  letter-spacing:.01em;transition:all .3s var(--ease);
}
.btn-primary{background:var(--teal);color:#fff;box-shadow:0 4px 14px rgba(47,92,95,.25)}
.btn-primary:hover{background:var(--teal-mid);transform:translateY(-3px);box-shadow:0 8px 24px rgba(47,92,95,.35)}
.btn-outline{border:1.5px solid var(--border2);color:var(--ink);background:var(--surface);backdrop-filter:blur(8px)}
.btn-outline:hover{background:var(--bg1);border-color:var(--teal);color:var(--teal);transform:translateY(-3px);box-shadow:var(--shadow)}
.btn-ghost{color:var(--teal);font-weight:600;font-size:.9rem;display:inline-flex;align-items:center;gap:6px;font-family:var(--font-head)}
.btn-ghost:hover{gap:12px}
.btn-ghost svg{transition:transform .3s var(--ease)}

/* ── NAV ────────────────────────────────────────────────── */
nav{
  position:fixed;top:0;left:0;right:0;z-index:100;
  padding:20px 0;transition:all .4s var(--ease);
}
nav.scrolled{
  background:rgba(255,255,255,0.7);backdrop-filter:blur(20px);
  border-bottom:1px solid var(--border);padding:14px 0;
  box-shadow:var(--shadow);
}
.nav-inner{display:flex;align-items:center;justify-content:space-between}
.nav-logo{display:flex;align-items:center;gap:12px}
.logo-image{height:40px;width:auto;object-fit:contain}
.logo-text{font-family:var(--font-head);font-size:.85rem;font-weight:700;letter-spacing:.02em;text-transform:uppercase;color:var(--ink);line-height:1.2}
.logo-text span{display:block;font-weight:500;color:var(--muted);letter-spacing:.04em;font-size:.7rem;font-family:var(--font-body)}
.nav-links{display:flex;align-items:center;gap:36px}
.nav-links a{
  font-size:.9rem;font-weight:600;color:var(--muted);
  transition:color .25s;position:relative;font-family:var(--font-head);
}
.nav-links a::after{
  content:'';position:absolute;bottom:-4px;left:0;right:0;height:2px;
  background:var(--teal);transform:scaleX(0);transition:transform .3s var(--ease);border-radius:2px;
}
.nav-links a:hover{color:var(--ink)}
.nav-links a:hover::after{transform:scaleX(1)}
.hamburger{display:none;flex-direction:column;gap:6px;padding:8px;cursor:pointer}
.hamburger span{width:24px;height:2px;background:var(--ink);transition:all .3s;border-radius:2px}

/* ── MOBILE MENU ────────────────────────────────────────── */
.mobile-menu{
  position:fixed;inset:0;z-index:99;
  background:rgba(255,255,255,0.9);backdrop-filter:blur(24px);
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px;
  transform:translateX(100%);transition:transform .5s var(--ease);
}
.mobile-menu.open{transform:none}
.mobile-menu a{font-family:var(--font-head);font-size:2.5rem;font-weight:800;color:var(--ink);transition:color .3s}
.mobile-menu a:hover{color:var(--teal)}

/* ── HERO ───────────────────────────────────────────────── */
#hero{
  min-height:100svh;display:flex;align-items:center;
  padding:140px 0 80px;
  background:
    radial-gradient(ellipse 60% 50% at 85% 40%, rgba(47,92,95,.06) 0%, transparent 60%),
    radial-gradient(ellipse 40% 40% at 15% 80%, rgba(47,92,95,.03) 0%, transparent 50%),
    var(--bg);
}
.hero-inner{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center}
.hero-eyebrow{
  display:inline-flex;align-items:center;gap:12px;margin-bottom:32px;
  padding:6px 14px;background:var(--bg1);border:1px solid var(--border);border-radius:20px;box-shadow:var(--shadow);
}
.hero-eyebrow .rule{margin:0;width:12px;height:12px;border-radius:50%}
h1 em.styled{display:block;background:linear-gradient(135deg, var(--ink), var(--teal));-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.hero-sub{font-size:1.1rem;margin:28px 0 44px;max-width:500px;color:var(--muted);line-height:1.8}
.hero-actions{display:flex;align-items:center;gap:16px;flex-wrap:wrap}

/* Hero right panel (Glassmorphism concept) */
.hero-panel{
  background:var(--surface);backdrop-filter:blur(16px);
  border:1px solid rgba(255,255,255,0.8);
  border-radius:var(--r2);overflow:hidden;
  box-shadow:var(--shadow2);
  position:relative;
}
.hero-panel::before{
  content:'';position:absolute;inset:0;border-radius:var(--r2);
  padding:1px;background:linear-gradient(135deg,rgba(255,255,255,0.8),rgba(255,255,255,0));
  -webkit-mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);
  -webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none;
}
.panel-header{
  padding:18px 24px;border-bottom:1px solid var(--border);
  display:flex;align-items:center;justify-content:space-between;
  background:rgba(255,255,255,0.5);
}
.panel-title{font-family:var(--font-mono);font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink2);font-weight:600}
.panel-badge{
  padding:4px 12px;border-radius:20px;
  background:var(--teal-pale);color:var(--teal);
  font-family:var(--font-mono);font-size:.65rem;letter-spacing:.1em;font-weight:600;
}
.panel-badge::before{content:'● ';font-size:.65rem;color:var(--teal)}
.panel-body{padding:28px}
.terminal-line{
  display:flex;gap:12px;margin-bottom:10px;
  font-family:var(--font-mono);font-size:.75rem;line-height:1.6;
}
.t-prompt{color:var(--teal);flex-shrink:0;font-weight:bold}
.t-cmd{color:var(--ink);font-weight:600}
.t-out{color:var(--muted)}
.t-ok{color:var(--teal-lt);font-weight:600}
.t-warn{color:#d97706;font-weight:600}
.t-cursor{display:inline-block;width:8px;height:14px;background:var(--teal);animation:blink 1s infinite;vertical-align:middle;border-radius:1px}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}

/* availability strip below terminal */
.panel-strip{
  padding:16px 24px;border-top:1px solid var(--border);
  background:rgba(255,255,255,0.4);
  display:flex;align-items:center;gap:12px;
}
.strip-dot{width:8px;height:8px;border-radius:50%;background:var(--teal);animation:pulse 2s infinite;flex-shrink:0;box-shadow:0 0 8px var(--teal-lt)}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}
.panel-strip span{font-family:var(--font-mono);font-size:.7rem;color:var(--ink2);font-weight:600}

/* ── TRUST BAR ──────────────────────────────────────────── */
#trust{
  padding:32px 0;
  background:var(--bg1);border-top:1px solid var(--border);border-bottom:1px solid var(--border);
}
.trust-inner{display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:48px}
.trust-item{
  display:flex;align-items:center;gap:12px;
  font-family:var(--font-head);font-size:.85rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);
}
.trust-icon{
  width:32px;height:32px;
  display:flex;align-items:center;justify-content:center;color:var(--teal);
}

/* ── SERVICES ───────────────────────────────────────────── */
#services{padding:140px 0}
.section-header{margin-bottom:80px;text-align:center;display:flex;flex-direction:column;align-items:center}
.section-header .rule{margin:24px auto}
.section-header p{max-width:600px;font-size:1.1rem;margin:0 auto}

/* Bento Style Grid */
.bento-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 32px;
}

.service-block{
  border:1px solid var(--border);border-radius:var(--r2);
  overflow:hidden;background:var(--bg1);
  box-shadow:var(--shadow);
  transition:all .4s var(--ease);
  display:flex;flex-direction:column;
}
.service-block:hover{box-shadow:var(--shadow2);transform:translateY(-4px);border-color:var(--border2)}

.sb-visual{
  background:var(--bg2);position:relative;overflow:hidden;height:240px;
  display:flex;align-items:center;justify-content:center;
  border-bottom:1px solid var(--border);
}

/* Decorative abstract for each service */
.vis-grid{
  position:absolute;inset:0;
  background-image:linear-gradient(rgba(15,23,42,.03) 1px,transparent 1px),
    linear-gradient(90deg, rgba(15,23,42,.03) 1px,transparent 1px);
  background-size:24px 24px;
}
.vis-node{
  width:64px;height:64px;border-radius:18px;
  background:var(--teal);
  display:flex;align-items:center;justify-content:center;
  color:#fff;position:relative;z-index:1;
  box-shadow:0 12px 32px rgba(47,92,95,.25);
}

.sb-content{padding:48px;display:flex;flex-direction:column;flex-grow:1}
.sb-num{font-family:var(--font-mono);font-size:.7rem;letter-spacing:.15em;text-transform:uppercase;color:var(--teal-lt);margin-bottom:12px;font-weight:600}
.sb-sub{margin-bottom:12px;display:block}
.sb-content h3{font-size:1.8rem;margin-bottom:20px;font-weight:800}
.sb-content p{font-size:1rem;line-height:1.7;margin-bottom:32px;flex-grow:1}
.sb-features{display:flex;flex-direction:column;gap:12px;margin-bottom:36px}
.sb-feat{display:flex;align-items:center;gap:12px;font-size:.9rem;color:var(--ink);font-weight:600}
.feat-dot{width:6px;height:6px;border-radius:50%;background:var(--teal);flex-shrink:0}

/* two-column smaller cards for security sub-features */
.sb-mini-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:32px}
.sb-mini{
  padding:20px;border-radius:var(--r);
  background:var(--bg2);border:1px solid var(--border);
}
.sb-mini h4{font-size:.9rem;font-weight:700;margin-bottom:8px;font-family:var(--font-head);color:var(--ink)}
.sb-mini p{font-size:.85rem;line-height:1.6;color:var(--muted);margin:0}

/* ── METRICS ────────────────────────────────────────────── */
#metrics{
  padding:100px 0;
  background:var(--bg1);
  border-top:1px solid var(--border);border-bottom:1px solid var(--border);
  position:relative;overflow:hidden;
}
#metrics::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,var(--teal),transparent);opacity:0.2}
.metrics-inner{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;}
.met{
  background:var(--surface);padding:48px 32px;text-align:center;
  border-radius:var(--r2);border:1px solid var(--border);
  transition:all .4s var(--ease);position:relative;
}
.met:hover{transform:translateY(-5px);box-shadow:var(--shadow2);border-color:var(--teal-pale)}
.met-val{
  font-family:var(--font-head);font-size:3.5rem;font-weight:900;
  color:var(--teal);line-height:1;margin-bottom:12px;letter-spacing:-.03em;
}
.met-label{font-family:var(--font-head);font-size:.85rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:var(--ink2)}

/* ── PROCESS ────────────────────────────────────────────── */
#process{padding:140px 0;background:var(--bg)}
.process-header{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:start;margin-bottom:100px}
.process-badge{
  padding:8px 16px;border-radius:20px;
  background:var(--teal-pale);border:1px solid var(--teal-pale2);
  font-family:var(--font-mono);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--teal);font-weight:700;
  display:inline-block;margin-bottom:24px;
}
.process-right p{font-size:1.1rem;color:var(--muted);line-height:1.8;margin-bottom:24px}
.blockquote{
  border-left:3px solid var(--teal);padding-left:24px;
  font-family:var(--font-head);font-size:1.15rem;font-style:normal;font-weight:600;color:var(--ink);
  line-height:1.6;margin-top:32px;background:linear-gradient(90deg, var(--teal-pale), transparent);padding:24px;border-radius:0 var(--r) var(--r) 0;
}
.blockquote cite{display:block;margin-top:12px;font-style:normal;font-family:var(--font-mono);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--teal);font-weight:700}

/* Phase cards */
.phases{display:flex;flex-direction:column;gap:40px;position:relative}
.phases::before{
  content:'';position:absolute;left:40px;top:0;bottom:0;width:2px;
  background:var(--border);border-radius:2px;
}
.phase{
  display:grid;grid-template-columns:120px 1fr;gap:48px;align-items:start;
  position:relative;
}
.phase-label{
  position:sticky;top:120px;display:flex;flex-direction:column;align-items:center;
  background:var(--bg);padding:10px 0;
}
.phase-num{
  font-family:var(--font-head);font-size:2rem;font-weight:900;
  color:#fff;background:var(--teal);width:64px;height:64px;border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 8px 24px rgba(47,92,95,.25);z-index:2;
}
.phase-content{
  background:var(--bg1);border:1px solid var(--border);border-radius:var(--r2);padding:48px;
  box-shadow:var(--shadow);transition:all .3s var(--ease);
}
.phase-content:hover{box-shadow:var(--shadow2);border-color:var(--border2)}
.phase-content h3{font-size:1.8rem;margin-bottom:16px;font-weight:800}
.phase-content p{font-size:1.05rem;line-height:1.8;margin-bottom:32px}
.phase-items{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.phase-item{
  padding:24px;border-radius:var(--r);
  background:var(--bg2);border:1px solid transparent;
  transition:all .25s;
}
.phase-item:hover{border-color:var(--teal-lt);background:white;box-shadow:var(--shadow)}
.phase-item h4{font-size:1rem;font-weight:700;margin-bottom:8px;font-family:var(--font-head);color:var(--ink)}
.phase-item p{font-size:.9rem;color:var(--muted);margin:0;line-height:1.6}

/* Phase 2 — ROI cards */
.roi-cards{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-bottom:28px}
.roi-card{
  padding:32px;border-radius:var(--r);
  background:var(--bg2);border:1px solid var(--border);
}
.roi-card .rc-label{font-family:var(--font-mono);font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:12px;font-weight:600}
.roi-card .rc-val{font-family:var(--font-head);font-size:2.8rem;font-weight:800;color:var(--teal);margin-bottom:12px;display:flex;align-items:baseline;gap:8px}
.roi-track{height:6px;background:var(--border);border-radius:3px;overflow:hidden;margin-bottom:16px}
.roi-fill{height:100%;background:var(--teal);border-radius:3px;transition:width 1.4s var(--ease);width:0}
.roi-card p{font-size:.9rem;color:var(--muted);margin:0;line-height:1.6}
.phase-tags{display:flex;gap:12px;flex-wrap:wrap}
.ptag{
  padding:6px 16px;border-radius:20px;
  background:var(--teal-pale);border:1px solid var(--teal-pale2);
  font-family:var(--font-head);font-size:.8rem;font-weight:600;color:var(--teal);
}

/* Phase 3 — timeline */
.roadmap-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;}
.rm-card{
  padding:28px;border-radius:var(--r);
  background:var(--bg2);border:1px solid var(--border);
  transition:all .3s ease;
}
.rm-card:hover{border-color:var(--teal-lt);background:white;transform:translateY(-3px);box-shadow:var(--shadow)}
.rm-period{font-family:var(--font-mono);font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--teal);margin-bottom:12px;font-weight:700}
.rm-card h4{font-size:1.1rem;font-weight:800;margin-bottom:10px;font-family:var(--font-head);color:var(--ink)}
.rm-card p{font-size:.9rem;color:var(--muted);margin:0;line-height:1.6}

/* ── DISCOVERY CTA BLOCK ────────────────────────────────── */
#discovery{
  padding:120px 0;
  background:var(--bg1);border-top:1px solid var(--border);
}
.discovery-inner{
  background:linear-gradient(135deg, var(--teal), var(--ink));
  border-radius:var(--r2);
  padding:80px 100px;
  display:grid;grid-template-columns:1fr auto;gap:60px;align-items:center;
  overflow:hidden;position:relative;
  box-shadow:0 24px 48px rgba(15,23,42,.15);
}
.disc-bg{
  position:absolute;right:-80px;top:-80px;
  width:400px;height:400px;border-radius:50%;
  background:radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
}
.discovery-inner h2{color:#fff;font-size:clamp(2rem,3.5vw,3rem);margin-bottom:20px}
.discovery-inner p{color:rgba(255,255,255,.8);font-size:1.1rem;line-height:1.8;max-width:520px}
.disc-cta{flex-shrink:0;position:relative;z-index:1}
.btn-white{background:#fff;color:var(--teal);font-weight:700;padding:16px 36px;border-radius:var(--r);display:inline-flex;align-items:center;gap:12px;transition:all .3s var(--ease);white-space:nowrap;font-size:1rem}
.btn-white:hover{transform:translateY(-3px);box-shadow:0 12px 32px rgba(0,0,0,.2)}
.btn-white-outline{border:2px solid rgba(255,255,255,.3);color:#fff;background:transparent;padding:16px 36px;border-radius:var(--r);display:inline-flex;align-items:center;justify-content:center;gap:8px;font-weight:600;font-size:1rem;transition:all .3s;white-space:nowrap;margin-top:16px}
.btn-white-outline:hover{background:rgba(255,255,255,.1);border-color:#fff}
.disc-cta-btns{display:flex;flex-direction:column;gap:0}

/* ── QUOTE FORM ─────────────────────────────────────────── */
#quote{padding:140px 0;background:var(--bg)}
.quote-grid{display:grid;grid-template-columns:1fr 1.3fr;gap:80px;align-items:start}
.quote-left .label{display:block;margin-bottom:16px}
.quote-left h2{margin-bottom:24px}
.quote-left p{font-size:1.05rem;line-height:1.8;margin-bottom:40px}
.ql-quote{
  background:var(--bg1);border:1px solid var(--border);border-left:4px solid var(--teal);
  padding:32px;border-radius:0 var(--r) var(--r) 0;
  margin-bottom:40px;box-shadow:var(--shadow);
}
.ql-quote p{
  font-family:var(--font-head);font-style:normal;font-weight:600;font-size:1.15rem;
  color:var(--ink);margin:0;line-height:1.6;
}
.ql-quote cite{display:block;margin-top:16px;font-style:normal;font-family:var(--font-mono);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--teal);font-weight:700}
.ql-secure{
  display:flex;align-items:center;gap:16px;
  padding:20px;border-radius:var(--r);
  border:1px solid var(--border);background:var(--bg1);
}
.ql-secure-icon{
  width:44px;height:44px;border-radius:12px;flex-shrink:0;
  background:var(--teal-pale);color:var(--teal);
  display:flex;align-items:center;justify-content:center;
}
.ql-secure-text{font-size:.9rem}
.ql-secure-text strong{display:block;font-weight:700;color:var(--ink);font-size:.95rem;margin-bottom:4px}
.ql-secure-text span{color:var(--muted);font-size:.85rem;line-height:1.5}

/* Form */
.quote-form{
  background:var(--bg1);border:1px solid var(--border);
  border-radius:var(--r2);padding:48px;
  box-shadow:var(--shadow2);
}
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.form-group{margin-bottom:24px}
.form-label{
  display:block;font-family:var(--font-head);font-size:.85rem;font-weight:700;
  color:var(--ink);margin-bottom:10px;
}
.form-input{
  width:100%;padding:14px 18px;
  background:var(--bg2);border:2px solid transparent;
  border-radius:var(--r);color:var(--ink);font-size:.95rem;
  transition:all .3s;outline:none;font-family:var(--font-body);
}
.form-input:hover{background:var(--border)}
.form-input:focus{border-color:var(--teal);background:var(--bg1);box-shadow:0 0 0 4px rgba(47,92,95,0.1)}
.form-input::placeholder{color:var(--muted);opacity:1}
select.form-input{cursor:pointer;appearance:none;background-image:url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%2364748b%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E");background-repeat:no-repeat;background-position:right .7em top 50%;background-size:.65em auto}
textarea.form-input{resize:vertical;min-height:140px}

/* Service pills inside form */
.service-pills{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.sp{
  padding:12px;border-radius:8px;
  border:2px solid var(--border);background:var(--bg1);
  cursor:pointer;transition:all .2s;text-align:center;
  font-size:.85rem;font-weight:600;color:var(--muted);
}
.sp:hover{border-color:var(--teal-pale2);color:var(--ink);background:var(--bg2)}
.sp.sel{border-color:var(--teal);color:var(--teal);background:var(--teal-pale)}

.form-submit-row{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;margin-top:16px}
.form-note{font-family:var(--font-body);font-size:.85rem;color:var(--muted);font-weight:500}

/* Success state */
.form-success{display:none;text-align:center;padding:40px 0;animation:fadeIn .5s var(--ease)}
.success-circle{
  width:80px;height:80px;border-radius:50%;
  background:var(--teal-pale);color:var(--teal);
  display:flex;align-items:center;justify-content:center;
  margin:0 auto 24px;font-size:2rem;
}
@keyframes fadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}

/* Credentials below form */
.cred-strip{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:40px}
.cred{
  padding:24px;border-radius:var(--r);
  background:var(--bg1);border:1px solid var(--border);
  transition:all .3s;
}
.cred:hover{border-color:var(--teal-pale2);box-shadow:var(--shadow)}
.cred-icon{
  width:40px;height:40px;border-radius:10px;
  background:var(--bg2);color:var(--teal);
  display:flex;align-items:center;justify-content:center;
  margin-bottom:16px;
}
.cred h4{font-size:.95rem;font-weight:800;margin-bottom:8px;font-family:var(--font-head)}
.cred p{font-size:.85rem;color:var(--muted);margin:0;line-height:1.6}

/* ── FOOTER ─────────────────────────────────────────────── */
footer{
  padding:80px 0 40px;
  border-top:1px solid var(--border);
  background:var(--bg1);
}
.footer-top{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:60px;margin-bottom:60px}
.footer-brand .logo-image{height:40px;width:auto;object-fit:contain;margin-bottom:20px;filter:grayscale(100%) opacity(0.8);transition:all .3s}
.footer-brand .logo-image:hover{filter:none}
.logo-mark{display:none}
.footer-brand .logo-text{color:var(--ink);font-weight:800}
.footer-brand .logo-text span{color:var(--muted)}
.footer-brand p{font-size:.95rem;color:var(--muted);margin-top:16px;max-width:280px;line-height:1.8}
.footer-col h5{font-family:var(--font-head);font-size:.85rem;font-weight:800;color:var(--ink);margin-bottom:24px}
.footer-col ul{display:flex;flex-direction:column;gap:14px}
.footer-col ul li a{font-size:.95rem;color:var(--muted);font-weight:500;transition:color .2s}
.footer-col ul li a:hover{color:var(--teal)}
.footer-bottom{
  display:flex;align-items:center;justify-content:space-between;
  padding-top:32px;border-top:1px solid var(--border);flex-wrap:wrap;gap:16px;
}
.footer-copy{font-family:var(--font-body);font-size:.85rem;color:var(--muted);font-weight:500}
.footer-socials{display:flex;gap:12px}
.social-btn{
  width:40px;height:40px;border-radius:8px;
  border:1px solid var(--border);background:var(--bg2);
  display:flex;align-items:center;justify-content:center;
  color:var(--muted);transition:all .3s;
}
.social-btn:hover{border-color:var(--teal);color:var(--teal);background:var(--bg1);transform:translateY(-2px)}

/* ── RESPONSIVE ─────────────────────────────────────────── */
@media(max-width:1024px){
  .hero-inner{grid-template-columns:1fr;gap:40px}
  .bento-grid {grid-template-columns: 1fr}
  .sb-visual{height:200px}
  .sb-mini-grid{grid-template-columns:1fr}
  .metrics-inner{grid-template-columns:repeat(2,1fr)}
  .process-header{grid-template-columns:1fr;gap:40px}
  .phase{grid-template-columns:1fr;gap:24px}
  .phase-label{position:static;flex-direction:row;justify-content:space-between;background:transparent;padding:0}
  .roadmap-grid{grid-template-columns:1fr}
  .roi-cards{grid-template-columns:1fr}
  .quote-grid{grid-template-columns:1fr;gap:60px}
  .discovery-inner{grid-template-columns:1fr;padding:60px 40px;text-align:center}
  .disc-cta{margin:0 auto}
  .footer-top{grid-template-columns:1fr 1fr;gap:40px}
  .cred-strip{grid-template-columns:1fr}
  .nav-links{display:none}
  nav .btn{display:none}
  .hamburger{display:flex}
  .phases::before{display:none}
}
@media(max-width:600px){
  .metrics-inner{grid-template-columns:1fr;gap:16px}
  .phase-items{grid-template-columns:1fr}
  .footer-top{grid-template-columns:1fr}
  .form-row{grid-template-columns:1fr}
  .service-pills{grid-template-columns:1fr}
  .discovery-inner{padding:40px 24px}
  .hero-actions{flex-direction:column;align-items:stretch}
  .hero-actions .btn{width:100%;justify-content:center}
}
"""

    # Replace <style> block
    html_content = re.sub(r'<style>.*?</style>', f'<style>\n{new_css}\n</style>', html_content, flags=re.DOTALL)
    
    # Fonts update: switch Playfair/Instrument to Inter/Plus Jakarta Sans
    old_fonts = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,800;0,900;1,700;1,800&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'
    new_fonts = '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">'
    if old_fonts in html_content:
        html_content = html_content.replace(old_fonts, new_fonts)
    else:
        # Fallback regex replace for any google fonts link containing Playfair
        html_content = re.sub(r'<link href="https://fonts.googleapis.com[^>]*family=Playfair[^>]*>', new_fonts, html_content)

    # Wrap service blocks in bento-grid
    # Since it's a bit tricky to wrap with regex, I'll just change the container class or add the wrapper manually.
    # The structure is: div.section-header ... then div.service-block ... div.service-block ...
    # Let's replace the first `<div class="service-block reveal">` with `<div class="bento-grid">\n    <div class="service-block reveal">`
    # And then `<div class="service-block reverse reveal">` (the 4th one) needs a closing `</div>` after it.
    if '<div class="bento-grid">' not in html_content:
        html_content = html_content.replace('<!-- SaaS -->', '<!-- Bento Start -->\n    <div class="bento-grid">\n    <!-- SaaS -->')
        html_content = html_content.replace('</section>\n\n<!-- METRICS -->', '    </div>\n  </div>\n</section>\n\n<!-- METRICS -->')

    # Security reverse block has hardcoded inline styles for dark mode. Let's strip them or change them.
    # <div class="sb-visual" style="background:var(--ink);border-right:none;border-left:1px solid var(--border)">
    html_content = re.sub(r'<div class="sb-visual" style="background:var\(--ink\)[^>]*>', '<div class="sb-visual">', html_content)
    # <div class="sb-visual" style="background:var(--teal);border-right:none;border-left:1px solid var(--border)">
    html_content = re.sub(r'<div class="sb-visual" style="background:var\(--teal\)[^>]*>', '<div class="sb-visual">', html_content)
    
    # Same for internal visual elements that forced dark backgrounds or light texts
    html_content = html_content.replace('color:rgba(255,255,255,.3)', 'color:var(--muted)')
    html_content = html_content.replace('color:rgba(255,255,255,.4)', 'color:var(--muted)')
    html_content = html_content.replace('color:rgba(255,255,255,.6)', 'color:var(--ink)')
    html_content = html_content.replace('color:rgba(255,255,255,.7)', 'color:var(--ink)')
    html_content = html_content.replace('color:rgba(255,255,255,.8)', 'color:var(--ink)')
    html_content = html_content.replace('color:rgba(255,255,255,.9)', 'color:var(--ink)')
    html_content = html_content.replace('background:rgba(255,255,255,.08)', 'background:var(--bg1)')
    html_content = html_content.replace('background:rgba(255,255,255,.1)', 'background:var(--bg1)')
    html_content = html_content.replace('background:rgba(255,255,255,.03)', 'background:var(--bg1)')
    html_content = html_content.replace('border:1px solid rgba(255,255,255,.15)', 'border:1px solid var(--border)')
    html_content = html_content.replace('border:1px solid rgba(255,255,255,.2)', 'border:1px solid var(--border)')
    html_content = html_content.replace('border:1px solid rgba(255,255,255,.1)', 'border:1px solid var(--border)')
    
    # Fix the footer text inline styles and logo styling since we moved to light mode
    html_content = html_content.replace('style="color:rgba(255,255,255,.7)"', '')
    html_content = html_content.replace('style="color:rgba(255,255,255,.35)"', '')
    html_content = html_content.replace('filter:grayscale(100%) opacity(0.8)', '')

    # Write back
    with open(target_file, "w", encoding="utf-8") as file:
        file.write(html_content)
    print("Redesign applied to", target_file)

if __name__ == "__main__":
    rewrite()
