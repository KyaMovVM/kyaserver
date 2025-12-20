const VisualNovel = require('../Main/Japanese game/novel.js');

// Mock DOM implementation without jsdom
class MockElement {
  constructor(tag) {
    this.tag = tag;
    this.textContent = '';
    this.innerHTML = '';
    this.onclick = null;
    this.children = [];
    this.parent = null;
  }

  appendChild(child) {
    child.parent = this;
    this.children.push(child);
  }

  remove() {
    if (this.parent) {
      const idx = this.parent.children.indexOf(this);
      if (idx > -1) {
        this.parent.children.splice(idx, 1);
      }
    }
  }

  click() {
    if (this.onclick) {
      this.onclick();
    }
  }

  querySelector(selector) {
    if (selector === 'h3') return this.children.find(c => c.tag === 'h3') || null;
    if (selector === 'p') return this.children.find(c => c.tag === 'p') || null;
    if (selector === 'button') return this.children.find(c => c.tag === 'button') || null;
    return null;
  }

  querySelectorAll(selector) {
    if (selector === 'h3') return this.children.filter(c => c.tag === 'h3');
    if (selector === 'p') return this.children.filter(c => c.tag === 'p');
    if (selector === 'button') return this.children.filter(c => c.tag === 'button');
    return [];
  }
}

describe('VisualNovel', () => {
  let container;
  let mockDocument;

  beforeEach(() => {
    // Create mock DOM
    container = new MockElement('div');
    container.id = 'novel-container';

    mockDocument = {
      getElementById: (id) => id === 'novel-container' ? container : null,
      createElement: (tag) => new MockElement(tag),
      body: { appendChild: () => {} }
    };

    global.document = mockDocument;
  });

  test('renders first scene and shows next button', () => {
    const scenes = [
      { speaker: 'A', text: 'Hello' },
      { speaker: 'B', text: 'Hi' }
    ];
    const dlg = new VisualNovel(scenes);
    dlg.start();
    expect(container.querySelector('h3').textContent).toBe('A');
    expect(container.querySelector('p').textContent).toBe('Hello');
    const btn = container.querySelector('button');
    expect(btn).not.toBeNull();
    expect(btn.textContent).toBe('次へ');
  });

  test('shows end message after last scene', (done) => {
    const scenes = [
      { speaker: 'A', text: 'Hello' }
    ];
    const dlg = new VisualNovel(scenes);
    dlg.start();
    expect(container.querySelector('h3').textContent).toBe('A');
    expect(container.querySelector('p').textContent).toBe('Hello');
    expect(container.querySelector('button')).toBeNull();
    // Wait for setTimeout to complete
    setTimeout(() => {
      expect(container.innerHTML).toContain('End of story.');
      done();
    }, 10);
  });

  test('renders scenes sequentially when clicking next', () => {
    const scenes = [
      { speaker: 'A', text: 'First' },
      { speaker: 'B', text: 'Second' },
      { speaker: 'C', text: 'Third' }
    ];
    const dlg = new VisualNovel(scenes);
    dlg.start();
    // After start, first scene should be present
    expect(container.querySelectorAll('h3')[0].textContent).toBe('A');
    expect(container.querySelectorAll('p')[0].textContent).toBe('First');
    // Find the next button and click it
    let btn = container.querySelector('button');
    expect(btn).not.toBeNull();
    btn.click();
    // Now second scene should be appended
    const h3s = container.querySelectorAll('h3');
    const ps = container.querySelectorAll('p');
    expect(h3s.length).toBe(2);
    expect(h3s[1].textContent).toBe('B');
    expect(ps[1].textContent).toBe('Second');
    // Click again for third scene
    btn = container.querySelector('button');
    btn.click();
    const h3s2 = container.querySelectorAll('h3');
    const ps2 = container.querySelectorAll('p');
    expect(h3s2.length).toBe(3);
    expect(h3s2[2].textContent).toBe('C');
    expect(ps2[2].textContent).toBe('Third');
    // After last scene, button should be removed
    expect(container.querySelector('button')).toBeNull();
  });
});
