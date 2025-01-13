document.querySelectorAll('.copy-btn').forEach(button => {
    button.addEventListener('click', () => {
        navigator.clipboard.writeText(button.dataset.copy).then(() => {
            const toast = document.createElement('div');
            toast.className = 'toast align-items-center text-bg-success border-0';
            toast.role = 'alert';
            toast.style.position = 'fixed';
            toast.style.top = '1rem';
            toast.style.right = '1rem';
            toast.style.zIndex = '1055';
            toast.innerHTML = `
                <div class="d-flex">
                    <div class="toast-body">Copied to clipboard!</div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>`;
            document.body.appendChild(toast);

            const bootstrapToast = new bootstrap.Toast(toast);
            bootstrapToast.show();

            toast.addEventListener('hidden.bs.toast', () => toast.remove());
        });
    });
});
