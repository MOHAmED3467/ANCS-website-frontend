<template>
  <section class="about-page">
    <div class="container">
      <div class="section-header">
        <span class="subtitle">About ANCS</span>
        <h1>Network Automation Made Simple</h1>
        <p class="main-desc">
          ANCS is the graduation project platform for planning, validating, and deploying network configurations with reduced risk and better lab productivity.
        </p>
      </div>
      <div class="philosophy-grid">
        <div class="p-card">
          <div class="p-icon"><i class="fas fa-bullseye"></i></div>
          <h3>Technical Vision</h3>
          <p>
            We simplify configuration workflows for networking students and operators,
            turning CLI complexity into guided automation that reduces errors and speeds deployment.
          </p>
        </div>
        <div class="p-card">
          <div class="p-icon blue"><i class="fas fa-shield-alt"></i></div>
          <h3>Why ANCS?</h3>
          <p>
            ANCS adds a smart validation layer, secure device connections, and audit-ready history
            so changes can be deployed confidently and recovered safely.
          </p>
        </div>
      </div>
      <div class="workflow-section">
        <div class="section-header">
          <h2>Operating Workflow</h2>
          <p>The journey of data within ANCS from discovery to execution</p>
        </div>
        <div class="workflow-steps">
          <div class="step-card">
            <div class="step-badge">01</div>
            <div class="step-icon"><i class="fas fa-search-nodes"></i></div>
            <h3>Device Discovery</h3>
            <p>Scan lab environments and local networks to register devices, collect interface data, and build inventory automatically.</p>
          </div>
          <div class="step-card">
            <div class="step-badge">02</div>
            <div class="step-icon purple"><i class="fas fa-terminal"></i></div>
            <h3>Smart Scripting</h3>
            <p>Create configuration workflows with reusable templates and guided command generation for multi-vendor devices.</p>
          </div>
          <div class="step-card">
            <div class="step-badge">03</div>
            <div class="step-icon green"><i class="fas fa-brain"></i></div>
            <h3>AI Validation</h3>
            <p>Review proposed changes before deployment to catch syntax issues, conflicts, and unsafe network operations.</p>
          </div>
          <div class="step-card">
            <div class="step-badge">04</div>
            <div class="step-icon orange"><i class="fas fa-rocket"></i></div>
            <h3>Safe Deployment</h3>
            <p>Push verified configurations via SSH/Telnet and keep rollback points for fast recovery.</p>
          </div>
        </div>
      </div>
      <div class="tech-highlights">
        <div class="section-header">
          <h2>Built with Industry Standards</h2>
          <p>The powerful technology stack behind our automation engine</p>
        </div>
        <div class="tech-cards-grid">
          <div class="tech-mini-card">
            <div class="mini-icon"><i class="fab fa-vuejs"></i></div>
            <h4>Frontend</h4>
            <span class="tech-tag">Vue 3 + Vuetify</span>
            <p>Delivers a responsive and polished interface for managing devices, configurations, and workflows.</p>
          </div>
          <div class="tech-mini-card">
            <div class="mini-icon"><i class="fas fa-cubes"></i></div>
            <h4>State & Routing</h4>
            <span class="tech-tag">Pinia + Vue Router</span>
            <p>Supports smooth navigation and centralized application state management for a fluid user experience.</p>
          </div>
          <div class="tech-mini-card">
            <div class="mini-icon"><i class="fas fa-user-shield"></i></div>
            <h4>Security</h4>
            <span class="tech-tag">Secure Sessions</span>
            <p>Designed to work with encrypted credentials and safe device connection workflows.</p>
          </div>
          <div class="tech-mini-card">
            <div class="mini-icon"><i class="fas fa-code"></i></div>
            <h4>Integration</h4>
            <span class="tech-tag">SSH / Telnet</span>
            <p>Focuses on network protocols and automation-ready configuration deployment.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
⋮----
<style scoped>
/* Main Background & Typography */
.about-page {
  min-height: 100vh;
  padding: 120px 20px 80px;
  background: transparent;
  color: var(--text-primary);
  font-family: 'Inter', sans-serif;
  overflow-x: hidden;
}
.container {
  max-width: 1200px;
  margin: 0 auto;
}
/* Header Styles */
.section-header {
  text-align: center;
  margin-bottom: 60px;
}
.subtitle {
  color: #42a5f5;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-size: 14px;
  display: block;
  margin-bottom: 15px;
}
h1 {
  color: var(--text-primary);
}
.main-desc {
  color: var(--text-muted);
  max-width: 800px;
  margin: 0 auto;
  font-size: 1.1rem;
  line-height: 1.7;
}
/* Philosophy Grid */
.philosophy-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 30px;
  margin-bottom: 100px;
}
.p-card {
  background: var(--card-bg);
  padding: 40px;
  border-radius: 24px;
  border: 1px solid var(--border-color);
  transition: transform 0.3s ease;
}
.p-card:hover {
  transform: translateY(-5px);
  background: var(--card-bg);
  border-color: rgba(66, 165, 245, 0.3);
}
.p-icon { font-size: 40px; color: #42a5f5; margin-bottom: 25px; }
.p-icon.blue { color: #2196f3; }
.p-card h3 { font-size: 24px; margin-bottom: 15px; color: var(--text-primary); }
.p-card p { color: var(--text-secondary); line-height: 1.6; }
/* Workflow Steps */
.workflow-steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 25px;
  margin-top: 50px;
}
.step-card {
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  padding: 35px 25px;
  border-radius: 20px;
  text-align: center;
  position: relative;
  transition: all 0.4s ease;
}
.step-card:hover {
  background: rgba(66, 165, 245, 0.05);
  border-color: #42a5f5;
}
.step-badge {
  position: absolute;
  top: -15px;
  left: 50%;
  transform: translateX(-50%);
  background: #42a5f5;
  color: var(--text-primary);
  width: 40px;
  height: 40px;
  border-radius: 12px;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 5px 15px rgba(66, 165, 245, 0.4);
}
.step-icon { font-size: 38px; color: #42a5f5; margin: 15px 0 20px; }
.step-icon.purple { color: #bb86fc; }
.step-icon.green { color: #03dac6; }
.step-icon.orange { color: #ffab40; }
.step-card h3 { font-size: 20px; margin-bottom: 12px; color: var(--text-primary); }
.step-card p { font-size: 14px; color: var(--text-secondary); line-height: 1.6; }
/* Tech Highlights (New Styles) */
.tech-highlights {
  margin-top: 120px;
}
.tech-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 20px;
}
.tech-mini-card {
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  padding: 30px 20px;
  border-radius: 24px;
  text-align: center;
  transition: all 0.3s ease;
}
.tech-mini-card:hover {
  background: var(--card-bg-hover);
  border-color: #42a5f5;
  transform: translateY(-8px);
}
.mini-icon {
  font-size: 32px;
  color: #42a5f5;
  margin-bottom: 15px;
}
.tech-mini-card h4 {
  font-size: 18px;
  color: var(--text-primary);
  margin-bottom: 8px;
}
.tech-tag {
  display: inline-block;
  font-size: 12px;
  font-weight: 700;
  color: #42a5f5;
  background: rgba(66, 165, 245, 0.1);
  padding: 4px 12px;
  border-radius: 50px;
  margin-bottom: 15px;
}
.tech-mini-card p {
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.5;
}
/* Mobile Adjustments */
@media (max-width: 768px) {
  .section-header h1 { font-size: 2rem; }
  .philosophy-grid { grid-template-columns: 1fr; }
  .workflow-steps { grid-template-columns: 1fr; gap: 40px; }
  .tech-cards-grid { grid-template-columns: 1fr; }
}
@media (max-width: 600px) {
  .about-page {
    padding: 90px 20px 60px;
  }
  .section-header {
    margin-bottom: 40px;
  }
  .section-header h1 {
    font-size: 1.5rem;
  }
  .section-header p {
    font-size: 14px;
  }
  .p-card,
  .tech-mini-card,
  .step-card {
    padding: 20px;
  }
  .p-card h3,
  .tech-mini-card h4,
  .step-card h3 {
    font-size: 16px;
  }
  .p-card p,
  .tech-mini-card p,
  .step-card p {
    font-size: 13px;
  }
}
</style>
