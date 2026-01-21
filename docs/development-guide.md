# Guía de Desarrollo

## Convenciones de Código

### Python (Backend)
- Usar snake_case para variables y funciones
- Usar PascalCase para clases
- Máximo 88 caracteres por línea (Black formatter)

### JavaScript (Mobile)
- Usar camelCase para variables y funciones
- Usar PascalCase para componentes React
- Usar Prettier para formateo

## Git Workflow

1. Crear branch desde develop: `git checkout -b feature/nombre`
2. Hacer commits descriptivos
3. Push y crear Pull Request
4. Revisar y mergear a develop

## Testing

- Backend: pytest
- Mobile: Jest
