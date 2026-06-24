<template>
  <section class="features">
    <div class="container">
      <div class="section-header">
        <span class="subtitle">Technology Stack</span>
        <h1>Technology Stack</h1>
        <p>ANCS is built on tools and protocols designed for networking labs, automation, and secure device access.</p>
      </div>
      <div class="tech-icons">
        <div class="tech-card">🐍 Python</div>
        <div class="tech-card">💚 Vue.js</div>
        <div class="tech-card">🖥️ PySide6</div>
        <div class="tech-card">🗄️ SQLite</div>
        <div class="tech-card">🔗 GNS3</div>
        <div class="tech-card">🔌 REST API</div>
        <div class="tech-card">✨ Gemini AI</div>
        <div class="tech-card">🔐 Paramiko</div>
        <div class="tech-card">🔒 SSH</div>
        <div class="tech-card">📡 Telnet</div>
        <div class="tech-card">🌐 Cisco IOS</div>
        <div class="tech-card">⚙️ Huawei VRP</div>
      </div>
      <div class="section-header">
        <h2>Core Features</h2>
      </div>
      <div class="feature-grid">
        <div class="feature-card">
          <h3>Guided Configuration Wizards</h3>
          <p>
            Generate complete Cisco IOS configurations for VLANs,
            OSPF, EIGRP, RIP, DHCP, ACLs and Inter-VLAN Routing
            from simple user inputs.
          </p>
        </div>
        <div class="feature-card">
          <h3>Deep GNS3 Integration</h3>
          <p>
            Discover network topologies automatically, manage nodes,
            synchronize configurations and interact directly with
            GNS3 through REST APIs.
          </p>
        </div>
        <div class="feature-card">
          <h3>AI Network Copilot</h3>
          <p>
            AI-powered assistant capable of network discovery,
            auditing, troubleshooting, deployment and
            connectivity tracing.
          </p>
        </div>
        <div class="feature-card">
          <h3>Multi-Protocol Communication</h3>
          <p>
            Support for SSH, Telnet and Serial connections with
            intelligent protocol handling.
          </p>
        </div>
        <div class="feature-card">
          <h3>Live Configuration Sync</h3>
          <p>
            Pull existing configurations from devices and
            automatically synchronize network state.
          </p>
        </div>
        <div class="feature-card">
          <h3>Bulk Deployment</h3>
          <p>
            Deploy configurations to multiple devices
            simultaneously with detailed reporting.
          </p>
        </div>
      </div>
    </div>
  </section>
</template>
<style scoped>
.features {
  min-height: 100vh;
  padding: 120px 20px 80px;
  background: transparent;
}
.container {
  max-width: 1400px;
  margin: 0 auto;
}
.section-header {
  text-align: center;
  margin-bottom: 40px;
}
.feature-stats {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 20px;
  margin-bottom: 60px;
}
.stat-box {
  border: 1px solid rgba(66, 165, 245, 0.18);
  border-radius: 18px;
  padding: 24px 20px;
  background: rgba(66, 165, 245, 0.05);
  text-align: center;
}
.stat-box span {
  display: block;
  font-size: 32px;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 10px;
}
.stat-box p {
  font-size: 14px;
  color: var(--text-muted);
  margin: 0;
}
.subtitle {
  display: inline-block;
  padding: 8px 20px;
  background: rgba(66, 165, 245, 0.1);
  border: 1px solid rgba(66, 165, 245, 0.3);
  border-radius: 50px;
  color: #42a5f5;
  font-size: 14px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 20px;
}
.section-header h1 {
  font-size: 56px;
  font-weight: 800;
  margin-bottom: 20px;
  color: var(--text-primary);
}
.section-header p {
  font-size: 20px;
  color: var(--text-muted);
  max-width: 600px;
  margin: 0 auto;
}
.tech-icons {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 16px;
  margin-bottom: 50px;
}
.tech-card {
  background: var(--card-bg);
  color: var(--text-primary);
  border: 1px solid var(--border-color);
  border-radius: 18px;
  padding: 18px 14px;
  text-align: center;
  font-weight: 700;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.03);
}
.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 30px;
  margin-top: 30px;
}
.feature-card {
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 24px;
  padding: 40px 30px;
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
}
.feature-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, #42a5f5, transparent);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.4s ease;
}
.feature-card:hover {
  transform: translateY(-10px);
  background: var(--card-bg-hover);
  border-color: rgba(66, 165, 245, 0.2);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}
.feature-card:hover::before {
  transform: scaleX(1);
}
.card-icon {
  width: 70px;
  height: 70px;
  background: linear-gradient(135deg, #42a5f5, #0077b6);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 25px;
  font-size: 28px;
  color: var(--text-primary);
  box-shadow: 0 10px 30px rgba(66, 165, 245, 0.3);
}
.card-icon.blue {
  background: linear-gradient(135deg, #2196f3, #1976d2);
  box-shadow: 0 10px 30px rgba(33, 150, 243, 0.3);
}
.card-icon.purple {
  background: linear-gradient(135deg, #9c27b0, #7b1fa2);
  box-shadow: 0 10px 30px rgba(156, 39, 176, 0.3);
}
.card-icon.green {
  background: linear-gradient(135deg, #4caf50, #388e3c);
  box-shadow: 0 10px 30px rgba(76, 175, 80, 0.3);
}
.card-icon.orange {
  background: linear-gradient(135deg, #ff9800, #f57c00);
  box-shadow: 0 10px 30px rgba(255, 152, 0, 0.3);
}
.card-icon.red {
  background: linear-gradient(135deg, #f44336, #d32f2f);
  box-shadow: 0 10px 30px rgba(244, 67, 54, 0.3);
}
.feature-card h3 {
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 15px;
  color: var(--text-primary);
}
.feature-card > p {
  font-size: 15px;
  color: var(--text-secondary);
  margin-bottom: 25px;
  line-height: 1.6;
}
.feature-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.feature-list li {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 14px;
  color: var(--text-muted);
  line-height: 1.5;
}
.feature-list li i {
  color: #4caf50;
  margin-top: 3px;
  font-size: 12px;
}
/* Responsive */
@media (max-width: 1200px) {
  .features-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 992px) {
  .feature-stats {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
@media (max-width: 768px) {
  .section-header h1 {
    font-size: 36px;
  }
  .features-grid {
    grid-template-columns: 1fr;
  }
  .feature-card {
    padding: 30px 25px;
  }
}
@media (max-width: 600px) {
  .features {
    padding: 90px 20px 60px;
  }
  .section-header {
    margin-bottom: 40px;
  }
  .section-header h1 {
    font-size: 28px;
  }
  .section-header p {
    font-size: 16px;
  }
  .feature-card {
    padding: 20px 16px;
  }
  .card-icon {
    width: 50px;
    height: 50px;
    font-size: 20px;
  }
  .feature-card h3 {
    font-size: 16px;
  }
  .feature-card p {
    font-size: 13px;
  }
  .feature-list li {
    font-size: 12px;
  }
}
</style>
