const CACHE_NAME = "kitsune-funzone-shell-v2";
const THREE_URL = "https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js";
const APP_SHELL = [
  "./",
  "./index.html",
  "./favicon.png",
  "./manifest.json"
];

self.addEventListener("install", (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    await cache.addAll(APP_SHELL);

    // Cache Three.js while online so the game engine can load offline later.
    // If the CDN is unavailable during installation, do not block the app shell.
    try {
      const response = await fetch(THREE_URL, { mode: "cors", cache: "no-cache" });
      if (response.ok && response.type !== "opaque") {
        await cache.put(THREE_URL, response);
      }
    } catch (error) {
      console.warn("Could not precache Three.js; open the game online once and reload.", error);
    }

    await self.skipWaiting();
  })());
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(
        keys.filter((key) => key.startsWith("kitsune-funzone-shell-") && key !== CACHE_NAME)
          .map((key) => caches.delete(key))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const request = event.request;
  if (request.method !== "GET") return;

  const url = new URL(request.url);

  // Only intercept the Three.js CDN module cross-origin; leave other CDNs untouched.
  if (url.href === THREE_URL) {
    event.respondWith((async () => {
      const cache = await caches.open(CACHE_NAME);
      const cached = await cache.match(THREE_URL);
      if (cached) return cached;
      const response = await fetch(request);
      if (response.ok && response.type !== "opaque") {
        await cache.put(THREE_URL, response.clone());
      }
      return response;
    })());
    return;
  }

  if (url.origin !== self.location.origin) return;

  if (request.mode === "navigate") {
    event.respondWith(
      fetch(request)
        .then((response) => {
          if (response.ok) {
            const copy = response.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put("./index.html", copy));
          }
          return response;
        })
        .catch(async () => (await caches.match(request)) || (await caches.match("./index.html")))
    );
    return;
  }

  event.respondWith(
    caches.match(request).then((cached) => cached || fetch(request).then((response) => {
      if (response.ok) {
        const copy = response.clone();
        caches.open(CACHE_NAME).then((cache) => cache.put(request, copy));
      }
      return response;
    }))
  );
});
