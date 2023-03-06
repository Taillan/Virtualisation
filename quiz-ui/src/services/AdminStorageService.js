export default {
  clear() {
    return window.localStorage.clear();
  },
  saveAdminToken(token) {
    window.localStorage.setItem("adminToken", token);
  },
  getAdminToken() {
    return window.localStorage.getItem("adminToken");
  },
};