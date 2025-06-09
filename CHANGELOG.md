# Changelog

## 1.6.3 (2025-06-09)

Full Changelog: [v1.6.2...v1.6.3](https://github.com/Svahnar/svahnar-python/compare/v1.6.2...v1.6.3)

### Features

* **api:** api update ([6335cda](https://github.com/Svahnar/svahnar-python/commit/6335cda983093170cbb13ffe83132903d4bddcb7))
* **client:** add follow_redirects request option ([e43906c](https://github.com/Svahnar/svahnar-python/commit/e43906cd67d964f8b14cf9f351193b3922fa1179))


### Bug Fixes

* **docs/api:** remove references to nonexistent types ([61619ee](https://github.com/Svahnar/svahnar-python/commit/61619eebecc05dff352a1300e3eab6af44d37f5c))
* **package:** support direct resource imports ([c2cf20d](https://github.com/Svahnar/svahnar-python/commit/c2cf20d11bd2e57175e8a4653bf3a9f61411a7b8))
* **pydantic v1:** more robust ModelField.annotation check ([161c228](https://github.com/Svahnar/svahnar-python/commit/161c228d12366f0be369cd7889a4f74ae2952f73))


### Chores

* broadly detect json family of content-type headers ([381bbec](https://github.com/Svahnar/svahnar-python/commit/381bbecdcb3c9627ef571d8c459de7c659fde4b2))
* **ci:** add timeout thresholds for CI jobs ([fe147ba](https://github.com/Svahnar/svahnar-python/commit/fe147ba121b2eec5939d52bb955dac348beddcef))
* **ci:** fix installation instructions ([6352602](https://github.com/Svahnar/svahnar-python/commit/6352602b66b2cb6da0fd5f5626b7cefc6e9be391))
* **ci:** only use depot for staging repos ([406c2a0](https://github.com/Svahnar/svahnar-python/commit/406c2a0b8750150c0db83b36eb3305a183ed25e1))
* **ci:** upload sdks to package manager ([1e8ccc0](https://github.com/Svahnar/svahnar-python/commit/1e8ccc07542134dcc808d54b9493e93a781ec48f))
* **client:** minor internal fixes ([d83ad2f](https://github.com/Svahnar/svahnar-python/commit/d83ad2fa93729ce55ff468907a87d522497c8c9b))
* configure new SDK language ([73d6aee](https://github.com/Svahnar/svahnar-python/commit/73d6aeec37b19d70a60a7803b6f192b8d4c4c037))
* **docs:** grammar improvements ([ca7f1c9](https://github.com/Svahnar/svahnar-python/commit/ca7f1c992fc5ae1ca723a5a0f0829a6752e4dc40))
* **docs:** remove reference to rye shell ([572d23f](https://github.com/Svahnar/svahnar-python/commit/572d23f0e63cbe43d5cb447de9d7a5462271af58))
* **internal:** avoid errors for isinstance checks on proxies ([898ef79](https://github.com/Svahnar/svahnar-python/commit/898ef797d2847d9fab76d3cfb866b84b6b7b40e0))
* **internal:** base client updates ([e0c7337](https://github.com/Svahnar/svahnar-python/commit/e0c733726325939b58083bc78d08a5585608e0f9))
* **internal:** bump pyright version ([9d6b518](https://github.com/Svahnar/svahnar-python/commit/9d6b518f2540325ad2e94a35230aa6dbf25070be))
* **internal:** codegen related update ([033da64](https://github.com/Svahnar/svahnar-python/commit/033da64c34f3049a394ba3c16f2d255c37f97246))
* **internal:** codegen related update ([ef83211](https://github.com/Svahnar/svahnar-python/commit/ef83211bde2560432cdc6ceec6849b3f88e87dfa))
* **internal:** fix list file params ([c281500](https://github.com/Svahnar/svahnar-python/commit/c281500a94291134c5b62d312e3c04b5487a0ac6))
* **internal:** import reformatting ([513b53e](https://github.com/Svahnar/svahnar-python/commit/513b53e41b4f0de5241165f88797a323d55962d5))
* **internal:** refactor retries to not use recursion ([5a8d385](https://github.com/Svahnar/svahnar-python/commit/5a8d38530b4ca21c7e6787d8421ca721053237f8))
* **internal:** update models test ([958a582](https://github.com/Svahnar/svahnar-python/commit/958a5824f9b472b093f2005f28c48209ffd06ac7))
* **internal:** update pyright settings ([3f2cf4b](https://github.com/Svahnar/svahnar-python/commit/3f2cf4ba117b151e9455982d1346550a8678655c))

## 1.6.2 (2025-04-12)

Full Changelog: [v1.6.1...v1.6.2](https://github.com/Svahnar/svahnar-python/compare/v1.6.1...v1.6.2)

### Features

* **api:** api update ([2a45e7a](https://github.com/Svahnar/svahnar-python/commit/2a45e7ae508c9ba5ae31c47a49b7679607aa752b))

## 1.6.1 (2025-04-12)

Full Changelog: [v1.6.0...v1.6.1](https://github.com/Svahnar/svahnar-python/compare/v1.6.0...v1.6.1)

### Features

* **api:** api update ([2e0720d](https://github.com/Svahnar/svahnar-python/commit/2e0720dfb06e045bb5b7698387132c4882a87e15))


### Bug Fixes

* **perf:** optimize some hot paths ([0ebdfe3](https://github.com/Svahnar/svahnar-python/commit/0ebdfe3e4cb33fff5d14267e5b794501ad5eb758))
* **perf:** skip traversing types for NotGiven values ([5d8817e](https://github.com/Svahnar/svahnar-python/commit/5d8817e30393fb3361c42eea1c4f2945d6c0bb9b))

## 1.6.0 (2025-04-11)

Full Changelog: [v1.5.0...v1.6.0](https://github.com/Svahnar/svahnar-python/compare/v1.5.0...v1.6.0)

### Features

* **api:** api update ([431c247](https://github.com/Svahnar/svahnar-python/commit/431c247dd21e0b73277d36470904a1e59c37bcec))

## 1.5.0 (2025-04-10)

Full Changelog: [v1.4.0...v1.5.0](https://github.com/Svahnar/svahnar-python/compare/v1.4.0...v1.5.0)

### Features

* **api:** api update ([cf7508d](https://github.com/Svahnar/svahnar-python/commit/cf7508d01894f7eb8fc97c52d8cd183e191c49c5))


### Chores

* **internal:** expand CI branch coverage ([492bd0f](https://github.com/Svahnar/svahnar-python/commit/492bd0f1d969a16534e4cd2e379c5c9e75f73041))
* **internal:** reduce CI branch coverage ([f666714](https://github.com/Svahnar/svahnar-python/commit/f666714ba48db9151b5f6fac0fc55318219a1483))

## 1.4.0 (2025-04-09)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/Svahnar/svahnar-python/compare/v1.3.0...v1.4.0)

### Features

* **api:** api update ([#21](https://github.com/Svahnar/svahnar-python/issues/21)) ([2feec6d](https://github.com/Svahnar/svahnar-python/commit/2feec6d5ce4cbba891f9bdd2d7bcbab4e9b41428))

## 1.3.0 (2025-04-09)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/Svahnar/svahnar-python/compare/v1.2.0...v1.3.0)

### Features

* **api:** api update ([#19](https://github.com/Svahnar/svahnar-python/issues/19)) ([bee3de4](https://github.com/Svahnar/svahnar-python/commit/bee3de4b0b283b6f2c42b464f1a373def1c94822))

## 1.2.0 (2025-04-09)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/Svahnar/svahnar-python/compare/v1.1.0...v1.2.0)

### Features

* **api:** api update ([#14](https://github.com/Svahnar/svahnar-python/issues/14)) ([725168b](https://github.com/Svahnar/svahnar-python/commit/725168ba76812111a3d9713a437cb84ec32928c4))
* **api:** api update ([#18](https://github.com/Svahnar/svahnar-python/issues/18)) ([8f0719b](https://github.com/Svahnar/svahnar-python/commit/8f0719b187e3170b69a5927035cfd45cb86edd8e))
* **api:** manual updates ([#10](https://github.com/Svahnar/svahnar-python/issues/10)) ([3e61e54](https://github.com/Svahnar/svahnar-python/commit/3e61e54fc866fc4e9e995020c193657261b040f0))
* **api:** update via SDK Studio ([#5](https://github.com/Svahnar/svahnar-python/issues/5)) ([9adb118](https://github.com/Svahnar/svahnar-python/commit/9adb118b93546daab171919e7e05fba56e7cfdcd))


### Chores

* fix typos ([#8](https://github.com/Svahnar/svahnar-python/issues/8)) ([a23c194](https://github.com/Svahnar/svahnar-python/commit/a23c194a27c3b1e0c63ed66cf3cc52b7d3f84b2a))
* go live ([#1](https://github.com/Svahnar/svahnar-python/issues/1)) ([ec7ee3c](https://github.com/Svahnar/svahnar-python/commit/ec7ee3cffa0c4f3c5175c311a88079c31b2a29a8))
* **internal:** remove trailing character ([#12](https://github.com/Svahnar/svahnar-python/issues/12)) ([7c12256](https://github.com/Svahnar/svahnar-python/commit/7c12256d67a176fb25f1f3d3f6e7923eeb65c077))
* **internal:** slight transform perf improvement ([#15](https://github.com/Svahnar/svahnar-python/issues/15)) ([1fb0d08](https://github.com/Svahnar/svahnar-python/commit/1fb0d0840818f980c70c7fe07f6b6130ae51f983))
* slight wording improvement in README ([#17](https://github.com/Svahnar/svahnar-python/issues/17)) ([d2178f2](https://github.com/Svahnar/svahnar-python/commit/d2178f220907a4faf582a06f809d0e6434639c94))
* sync repo ([8508d3c](https://github.com/Svahnar/svahnar-python/commit/8508d3cc6cff7e92695af5b35a08ea06eabd1e13))
* update SDK settings ([#3](https://github.com/Svahnar/svahnar-python/issues/3)) ([be2bc47](https://github.com/Svahnar/svahnar-python/commit/be2bc47c168157dca68cb92686fbafcc584d8f6a))

## 1.1.0 (2025-04-08)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/Svahnar/svahnar-python/compare/v1.0.0...v1.1.0)

### Features

* **api:** api update ([#14](https://github.com/Svahnar/svahnar-python/issues/14)) ([725168b](https://github.com/Svahnar/svahnar-python/commit/725168ba76812111a3d9713a437cb84ec32928c4))


### Chores

* **internal:** remove trailing character ([#12](https://github.com/Svahnar/svahnar-python/issues/12)) ([7c12256](https://github.com/Svahnar/svahnar-python/commit/7c12256d67a176fb25f1f3d3f6e7923eeb65c077))

## 1.0.0 (2025-03-30)

Full Changelog: [v0.1.0-alpha.1...v1.0.0](https://github.com/Svahnar/svahnar-python/compare/v0.1.0-alpha.1...v1.0.0)

### Features

* **api:** manual updates ([#10](https://github.com/Svahnar/svahnar-python/issues/10)) ([3e61e54](https://github.com/Svahnar/svahnar-python/commit/3e61e54fc866fc4e9e995020c193657261b040f0))


### Chores

* fix typos ([#8](https://github.com/Svahnar/svahnar-python/issues/8)) ([a23c194](https://github.com/Svahnar/svahnar-python/commit/a23c194a27c3b1e0c63ed66cf3cc52b7d3f84b2a))

## 0.1.0-alpha.1 (2025-03-26)

Full Changelog: [v0.0.1-alpha.1...v0.1.0-alpha.1](https://github.com/Svahnar/svahnar-python/compare/v0.0.1-alpha.1...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([#5](https://github.com/Svahnar/svahnar-python/issues/5)) ([9adb118](https://github.com/Svahnar/svahnar-python/commit/9adb118b93546daab171919e7e05fba56e7cfdcd))

## 0.0.1-alpha.1 (2025-03-26)

Full Changelog: [v0.0.1-alpha.0...v0.0.1-alpha.1](https://github.com/Svahnar/svahnar-python/compare/v0.0.1-alpha.0...v0.0.1-alpha.1)

### Chores

* go live ([#1](https://github.com/Svahnar/svahnar-python/issues/1)) ([ec7ee3c](https://github.com/Svahnar/svahnar-python/commit/ec7ee3cffa0c4f3c5175c311a88079c31b2a29a8))
* sync repo ([8508d3c](https://github.com/Svahnar/svahnar-python/commit/8508d3cc6cff7e92695af5b35a08ea06eabd1e13))
* update SDK settings ([#3](https://github.com/Svahnar/svahnar-python/issues/3)) ([be2bc47](https://github.com/Svahnar/svahnar-python/commit/be2bc47c168157dca68cb92686fbafcc584d8f6a))
