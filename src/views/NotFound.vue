<template>
  <div class="not-found">
    <!-- Animated background grid -->
    <div class="grid-bg"></div>
    <!-- Glow orbs -->
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="content">
      <!-- Glitch 404 -->
      <div class="error-code" data-text="404">404</div>
      <div class="divider"></div>
      <h1 class="title">Page Not Found</h1>
      <p class="desc">
        The page you're looking for doesn't exist or has been moved.<br>
        Let's get you back on track.
      </p>
      <div class="actions">
        <router-link to="/" class="btn-primary">
          <i class="fas fa-home"></i> Back to Home
        </router-link>
        <router-link to="/contact" class="btn-ghost">
          <i class="fas fa-envelope"></i> Contact Support
        </router-link>
      </div>
      <!-- Quick links -->
      <div class="quick-links">
        <span class="ql-label">Quick links:</span>
        <router-link to="/features">Features</router-link>
        <router-link to="/download">Download</router-link>
        <router-link to="/team">Team</router-link>
        <router-link to="/about">About</router-link>
      </div>
    </div>
  </div>
</template>
⋮----
<!-- Animated background grid -->
⋮----
<!-- Glow orbs -->
⋮----
<!-- Glitch 404 -->
⋮----
<!-- Quick links -->
⋮----
<style scoped>
.not-found {
  min-height: 100vh;
  background: var(--body-bg);
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 40px 20px;
  position: relative;
  overflow: hidden;
}
/* Animated grid background */
.grid-bg {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(66,165,245,0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(66,165,245,0.04) 1px, transparent 1px);
  background-size: 60px 60px;
  mask-image: radial-gradient(ellipse 80% 80% at 50% 50%, black 40%, transparent 100%);
}
/* Glow orbs */
.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  pointer-events: none;
}
.orb-1 {
  width: 500px; height: 500px;
  background: radial-gradient(circle, rgba(66,165,245,0.08) 0%, transparent 70%);
  top: -150px; left: -150px;
}
.orb-2 {
  width: 400px; height: 400px;
  background: radial-gradient(circle, rgba(0,119,182,0.07) 0%, transparent 70%);
  bottom: -100px; right: -100px;
}
.content {
  position: relative;
  z-index: 1;
  max-width: 600px;
}
/* Glitch 404 */
.error-code {
  font-size: clamp(100px, 20vw, 160px);
  font-weight: 900;
  letter-spacing: -6px;
  line-height: 1;
  background: linear-gradient(135deg, #42a5f5 0%, #0077b6 50%, #42a5f5 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: var(--text-primary);
  position: relative;
  margin-bottom: 24px;
  animation: flicker 4s infinite;
}
/* Glitch layers */
.error-code::before,
.error-code::after {
  content: attr(data-text);
  position: absolute;
  top: 0; left: 0; right: 0;
  background: linear-gradient(135deg, #42a5f5, #0077b6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: var(--text-primary);
}
.error-code::before {
  animation: glitch-1 3s infinite;
  clip-path: polygon(0 0, 100% 0, 100% 35%, 0 35%);
  opacity: 0.6;
}
.error-code::after {
  animation: glitch-2 3s infinite;
  clip-path: polygon(0 65%, 100% 65%, 100% 100%, 0 100%);
  opacity: 0.4;
}
@keyframes glitch-1 {
  0%, 90%, 100% { transform: translate(0); }
  92% { transform: translate(-4px, 1px); }
  94% { transform: translate(4px, -1px); }
  96% { transform: translate(-2px, 2px); }
}
@keyframes glitch-2 {
  0%, 90%, 100% { transform: translate(0); }
  92% { transform: translate(4px, -1px); }
  94% { transform: translate(-4px, 1px); }
  96% { transform: translate(2px, -2px); }
}
@keyframes flicker {
  0%, 95%, 100% { opacity: 1; }
  96% { opacity: 0.8; }
  97% { opacity: 1; }
  98% { opacity: 0.7; }
}
.divider {
  width: 60px; height: 3px;
  background: linear-gradient(90deg, transparent, #42a5f5, transparent);
  margin: 0 auto 28px;
  border-radius: 2px;
}
.title {
  font-size: clamp(24px, 5vw, 36px);
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 16px;
  letter-spacing: -0.5px;
}
.desc {
  font-size: 16px;
  color: var(--text-secondary);
  line-height: 1.7;
  margin-bottom: 40px;
}
.actions {
  display: flex;
  gap: 14px;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 40px;
}
.btn-primary {
  display: inline-flex; align-items: center; gap: 9px;
  padding: 13px 28px;
  background: linear-gradient(135deg, #42a5f5, #0077b6);
  color: var(--text-primary); text-decoration: none;
  border-radius: 12px; font-size: 15px; font-weight: 600;
  transition: all 0.3s;
  box-shadow: 0 8px 25px rgba(0,119,182,0.3);
}
.btn-primary:hover { transform: translateY(-3px); box-shadow: 0 12px 30px rgba(0,119,182,0.45); }
.btn-ghost {
  display: inline-flex; align-items: center; gap: 9px;
  padding: 13px 28px;
  background: var(--card-bg);
  border: 1px solid rgba(255,255,255,0.12);
  color: rgba(255,255,255,0.75); text-decoration: none;
  border-radius: 12px; font-size: 15px; font-weight: 600;
  transition: all 0.3s;
}
.btn-ghost:hover { background: rgba(255,255,255,0.1); color: var(--text-primary); border-color: rgba(255,255,255,0.25); transform: translateY(-3px); }
.quick-links {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 8px 16px;
  padding-top: 28px;
  border-top: 1px solid rgba(255,255,255,0.06);
}
.ql-label { font-size: 13px; color: rgba(255,255,255,0.3); }
.quick-links a {
  font-size: 13.5px; color: rgba(255,255,255,0.55);
  text-decoration: none; font-weight: 500;
  transition: color 0.2s;
}
.quick-links a:hover { color: #42a5f5; }
@media (max-width: 600px) {
  .not-found {
    padding: 80px 16px;
  }
  .error-code {
    font-size: clamp(60px, 15vw, 100px);
    letter-spacing: -3px;
    margin-bottom: 16px;
  }
  .divider {
    width: 40px;
    margin-bottom: 20px;
  }
  .title {
    font-size: 24px;
    margin-bottom: 12px;
  }
  .desc {
    font-size: 14px;
    margin-bottom: 28px;
  }
  .actions {
    gap: 10px;
    margin-bottom: 28px;
  }
  .btn-primary,
  .btn-ghost {
    padding: 10px 20px;
    font-size: 13px;
  }
  .quick-links {
    flex-direction: column;
    gap: 8px;
    font-size: 12px;
  }
  .quick-links a {
    font-size: 12px;
  }
}
</style>